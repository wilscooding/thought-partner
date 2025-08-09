from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.elevenlabs import text_to_speech
from app.services.data import avatar_descriptions
from app.services.openrouter import call_openrouter_api
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()

converse_router = APIRouter()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

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

@converse_router.post("/converse/text")
async def converse_text(body: ConverseInput):
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

    # 3) Save MP3 and return URL
    os.makedirs("static/tts", exist_ok=True)
    filename = f"tts_{avatar['name'].replace(' ', '_')}.mp3"
    path = f"static/tts/{filename}"
    with open(path, "wb") as f:
        f.write(audio_bytes)

    return {
        "ai_response": ai_response,
        "audio_url": f"http://localhost:8000/{path}"  # adjust if you mount static differently
    }