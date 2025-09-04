# services/elevenlabs.py
import aiohttp
import httpx
import asyncio
import os
from typing import Dict, Optional
from dotenv import load_dotenv
from fastapi import HTTPException
from app.infra.http import client

load_dotenv()

ELEVEN_VOICES_URL = "https://api.elevenlabs.io/v1/voices"
ELEVEN_TTS_URL_TMPL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
ELEVEN_STT_URL = "https://api.elevenlabs.io/v1/speech-to-text"

VOICE_CACHE: Dict[str, str] = {}  # voice_id -> voice data dict

def _get_api_key() -> str:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ElevenLabs API key not configured.")
    return api_key

def _auth_headers() -> Dict[str, str]:
    return{"xi-api-key": _get_api_key()}


async def refresh_voice_cache():
    """Fetch voices from ElevenLabs and build a name->id map."""
    response = await client.get_retry(ELEVEN_VOICES_URL, headers=_auth_headers())
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Failed to list voices: {response.text}")
    
    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="Voices enpoint returned non JSON.")
    
    # Build cache using display_name (what you see in the UI)
    VOICE_CACHE.clear()
    for v in data.get("voices", []):
        display = (v.get("name") or v.get("display_name") or "").strip()
        vid = v.get("voice_id")
        if display and vid:
            VOICE_CACHE[display] = vid

def get_voice_id_by_name(voice_name: str) -> str:
    """Look up cached id by display name; raise helpful error if missing."""
    vid = VOICE_CACHE.get(voice_name)
    if not vid:
        raise HTTPException(
            status_code=400,
            detail=f'Voice "{voice_name}" not found in ElevenLabs account. '
                   f"Check your dashboard or update avatar voice_name."
        )
    return vid

# ---------- Speech to Text ----------
async def transcribe_audio(upload_file) -> str:
    """
    Sends the uploaded audio file straight to ElevenLabs STT.
    Handles both {"text": "..."} and {"transcriptions":[{"text":"..."}]} shapes.
    """

    # Be defensive about missing attrs
    filename = getattr(upload_file, "filename", None) or "audio"
    content_type = getattr(upload_file, "content_type", None) or "application/octet-stream"

    files = {
        "file": (filename, upload_file.file, content_type),
    }

    data = {"model_id": "scribe_v1"}

    try:
        response = await client.post_retry(ELEVEN_STT_URL, headers= _auth_headers, data=data, files=files)
        if response.status != 200:
                raise HTTPException(
                        status_code=502,
                        detail=f"STT provider error ({response.status_code}): {response.text}"
                    )

            # Parse JSON safely
        try:
            payload = response.json()
        
        except ValueError:
            raise HTTPException(status_code=502, detail="STT returned non JSON")
            
        # Shape 1: {"text": "..."}
        if isinstance(payload, dict) and isinstance(payload.get("text"), str):
            text = payload["text"].strip()
            if not text:
                raise HTTPException(status_code=502, detail="STT returned empty text.")
            return text

        # Shape 2: {"transcriptions":[{"text":"..."}]}
        trans = payload.get("transcriptions") if isinstance(payload, dict) else None
        if isinstance(trans, list) and trans:
            text = (trans[0] or {}).get("text", "")
            if isinstance(text, str) and text.strip():
                return text.strip()

        # Unknown shape: return payload to help debug
        raise HTTPException(status_code=502, detail=f"STT response unrecognized: {payload}")

    
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="STT request timed out.")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"STT network error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected STT error: {str(e)}")


# ---------- Text to Speech ----------
# services/elevenlabs.py
async def text_to_speech(text: str, *, voice_name: Optional[str] = None, voice_id: Optional[str] = None ) -> bytes:
    if not (voice_id or voice_name):
        raise HTTPException(status_code=400, detail="Provide voice_name or voice_id.")

    if not voice_id and voice_name:
        voice_id = get_voice_id_by_name(voice_name)

    url = ELEVEN_TTS_URL_TMPL.format(voice_id=voice_id)
    headers = _auth_headers()
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }

    try:
        resp = await client.post_retry(url, headers=headers, json=payload)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=f"TTS failed: {resp.text}")
        return resp.content  # MP3 bytes

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="TTS request timed out.")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"TTS network error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected TTS error: {str(e)}")     
