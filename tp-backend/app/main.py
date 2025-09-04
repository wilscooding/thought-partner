from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.converse import converse_router
from app.routes.prompt import router as prompt_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.stt import router as stt_router
from app.services.elevenlabs import refresh_voice_cache
from app.routes.health import router as health_router
import app.infra.env

app = FastAPI()


origins = [
    "http://localhost:8081",    # Expo Web
    "http://localhost:19006",   # Expo Go on web (optional)
    "http://127.0.0.1:8081",    # Alternate localhost
    "http://localhost:5173",    # Vite dev server
    "http://127.0.0.1:5173",
    "https://tp-frontend-dun.vercel.app",  # Deployed frontend
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can use ["*"] during development
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
