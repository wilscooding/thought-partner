# services/elevenlabs.py
import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not ELEVENLABS_API_KEY:
    raise RuntimeError("ELEVENLABS_API_KEY missing from environment")

VOICE_CACHE = {}  # voice_id -> voice data dict


async def refresh_voice_cache():
    """Fetch voices from ElevenLabs and build a name->id map."""
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    timeout = aiohttp.ClientTimeout(total=20)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status != 200:
                txt = await resp.text()
                raise HTTPException(status_code=502, detail=f"Failed to list voices: {txt}")
            data = await resp.json()

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
        # You can also choose a default here instead of erroring
        raise HTTPException(
            status_code=400,
            detail=f'Voice "{voice_name}" not found in ElevenLabs account. '
                   f"Check your dashboard or update avatar voice_name."
        )
    return vid

# ---------- Speech to Text ----------
async def transcribe_audio(audio_file):
    """
    Sends the uploaded audio file straight to ElevenLabs STT.
    Handles both {"text": "..."} and {"transcriptions":[{"text":"..."}]} shapes.
    """
    url = "https://api.elevenlabs.io/v1/speech-to-text"

    # Be defensive about missing attrs
    filename = getattr(audio_file, "filename", None) or "audio"
    content_type = getattr(audio_file, "content_type", None) or "application/octet-stream"

    form_data = aiohttp.FormData()
    form_data.add_field(
        "file",
        audio_file.file,
        filename=filename,
        content_type=content_type,
    )
    form_data.add_field("model_id", "scribe_v1")

    timeout = aiohttp.ClientTimeout(total=30)  # more headroom for mobile uploads

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                url,
                data=form_data,
                headers={"xi-api-key": ELEVENLABS_API_KEY},
            ) as response:
                if response.status != 200:
                    provider_text = await response.text()
                    raise HTTPException(
                        status_code=502,
                        detail=f"STT provider error ({response.status}): {provider_text}"
                    )

                # Parse JSON safely
                try:
                    data = await response.json()
                except Exception:
                    raw = await response.text()
                    raise HTTPException(status_code=502, detail=f"STT returned non-JSON: {raw}")

                # Shape 1: {"text": "..."}
                if isinstance(data, dict) and isinstance(data.get("text"), str):
                    text = data["text"].strip()
                    if not text:
                        raise HTTPException(status_code=502, detail="STT returned empty text.")
                    return text

                # Shape 2: {"transcriptions":[{"text":"..."}]}
                trans = data.get("transcriptions") if isinstance(data, dict) else None
                if isinstance(trans, list) and trans:
                    text = (trans[0] or {}).get("text", "")
                    if isinstance(text, str) and text.strip():
                        return text.strip()

                # Unknown shape: return payload to help debug
                raise HTTPException(status_code=502, detail=f"STT response unrecognized: {data}")

    except aiohttp.ClientResponseError as e:
        raise HTTPException(status_code=503, detail=f"STT client error: {str(e)}")
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="STT request timed out.")
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=503, detail=f"STT network error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected STT error: {str(e)}")


# ---------- Text to Speech ----------
# services/elevenlabs.py
async def text_to_speech(text: str, *, voice_name: str | None = None, voice_id: str | None = None) -> bytes:
    if not (voice_id or voice_name):
        raise HTTPException(status_code=400, detail="Provide voice_name or voice_id.")

    if not voice_id and voice_name:
        voice_id = get_voice_id_by_name(voice_name)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }

    timeout = aiohttp.ClientTimeout(total=20)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(url, json=payload, headers=headers) as response:
            if response.status != 200:
                error = await response.text()
                raise HTTPException(status_code=response.status, detail=f"TTS failed: {error}")
            return await response.read()

