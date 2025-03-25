from fastapi import FastAPI
from routes.prompt import router as prompt_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:8081",    # Expo Web
    "http://localhost:19006",   # Expo Go on web (optional)
    "http://127.0.0.1:8081",    # Alternate localhost
    "*"                         # (Optional: allow all for local dev)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can use ["*"] during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(prompt_router, prefix="/api", tags=["Thought Partner"])
