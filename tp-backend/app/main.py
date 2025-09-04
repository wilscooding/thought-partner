from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.converse import converse_router
from app.routes.prompt import router as prompt_router
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from app.routes.stt import router as stt_router
from app.services.elevenlabs import refresh_voice_cache
from app.routes.health import router as health_router
from app.core.settings import get_settings
import app.infra.env

settings = get_settings()
app = FastAPI(debug=settings.DEBUG)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,  # You can use ["*"] during development
    allow_origin_regex=settings.cors_origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.is_prod:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["https://tp-backend-ds4h.onrender.com", "https://tp-frontend-dun.vercel.app", "*.vercel.app"]
    )

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def _warm_voices():
    try:
        await refresh_voice_cache()
    except Exception as e:
        print("⚠️ Could not refresh ElevenLabs voices at startup:", e)

app.include_router(prompt_router, prefix="/api", tags=["Thought Partner"])
app.include_router(converse_router, prefix="/api", tags=["Converse"])
app.include_router(stt_router, prefix="/api", tags=["Speech to Text"])
app.include_router(health_router)
