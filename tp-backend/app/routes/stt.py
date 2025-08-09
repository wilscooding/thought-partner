# app/routes/stt.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.elevenlabs import transcribe_audio

router = APIRouter()

ALLOWED_BASE_TYPES = {"audio/webm", "audio/mpeg", "audio/mp4", "audio/ogg"}

@router.post("/stt")
async def handle_stt(audio: UploadFile = File(...)):
    raw_ct = (audio.content_type or "").lower()
    base_ct = raw_ct.split(";", 1)[0].strip()  # <-- normalize (drop ";codecs=opus")

    if not base_ct.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file: expected audio/* content-type.")

    if base_ct not in ALLOWED_BASE_TYPES:
        raise HTTPException(
            status_code=415,
            detail={
                "message": "Unsupported audio format.",
                "received": raw_ct,
                "allowed": sorted(list(ALLOWED_BASE_TYPES)),
                "hint": "Send WebM/Opus (Chrome), MP4/M4A (Safari), or MP3.",
            },
        )

    print("▶️ Upload received:", audio.filename)
    print("▶️ Content-Type:", raw_ct)

    try:
        audio.file.seek(0)
    except Exception:
        pass

    try:
        transcript = await transcribe_audio(audio)
        return {"transcript": transcript}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"STT upstream error: {str(e)}")
