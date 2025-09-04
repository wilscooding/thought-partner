from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.services.elevenlabs import text_to_speech
from app.services.data import avatar_descriptions
from app.services.openrouter import call_openrouter_api
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
import logging
from uuid import uuid4
from pathlib import Path

load_dotenv()

converse_router = APIRouter()

# elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

class ConverseInput(BaseModel):
    text: str
    selected_name: str



class ConverseResponse(BaseModel):
    ai_response: str
    audio_url: str | None = None

def _avatar_by_name(name: str):
    for a in avatar_descriptions:
        if a["name"].lower() == name.lower():
            return a
    return None

@converse_router.post("/converse/text", response_model=ConverseResponse)
async def converse_text(body: ConverseInput, request: Request):
    avatar = _avatar_by_name(body.selected_name)
    if not avatar:
        raise HTTPException(status_code=404, detail=f'Avatar "{body.selected_name}" not found.')

    # 1) Get AI content
    ai_response = await call_openrouter_api(body.text)

    # 2) TTS voice by avatar
    voice_name = avatar.get("voice_name")
    if not voice_name:
        # Optional default
        voice_name = "Bella"

    audio_bytes = await text_to_speech(ai_response, voice_name=voice_name)

    audio_url = None
    try:
        audio_bytes = await text_to_speech(ai_response, voice_name=voice_name)
        out_dir = Path("static/tts")
        out_dir.mkdir(parents=True, exist_ok=True)
        filename = f"tts_{avatar['name'].replace('', '_').lower()}_{uuid4().hex[:8]}.mp3"
        outh_path = out_dir / filename
        outh_path.write_bytes(audio_bytes)

        base = str(request.base_url).rstrip("/")
        audio_url = f"{base}/static/tts/{filename}"

    except Exception:
        logging.getLogger(__name__).warning(
            "TTS failed; returning text-only response.", exc_info=True
        )

    return {"ai_response": ai_response, "audio_url": audio_url}