from functools import lru_cache
from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    ENV: str = "development"            # set to "production" on Render
    DEBUG: bool = False                 # leave False in prod
    BACKEND_CORS_ORIGINS: str = ""      # comma-separated list; optional

    BACKEND_CORS_ORIGIN_REGEX: str = "" # optional regex pattern

    def _split_strip(self, s: str) -> List[str]:
        return [p.strip() for p in s.split(",") if p.strip()]

    # vendor keys (optional in dev)
    OPENROUTER_API_KEY: str | None = None
    OPENROUTER_HTTP_REFERER: str | None = None
    OPENROUTER_X_TITLE: str | None = None
    ELEVENLABS_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def is_prod(self) -> bool:
        return self.ENV.lower() in {"prod", "production"}

    @property
    def cors_origins(self) -> List[str]:
        if self.BACKEND_CORS_ORIGINS:
            return [o.strip() for o in self.BACKEND_CORS_ORIGINS.split(",") if o.strip()]
        # sensible defaults
        return (
            ["https://tp-frontend-dun.vercel.app"] if self.is_prod
            else [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:8081",     # Expo web
                "http://127.0.0.1:8081",
                "http://localhost:19006",    # Expo web (alt)
                "http://127.0.0.1:19006",
            ]
        )
    
    @property
    def cors_origin_regex(self) -> Optional[str]:
        if self.BACKEND_CORS_ORIGIN_REGEX:
            return self.BACKEND_CORS_ORIGIN_REGEX
        if self.is_prod:
            # Allow your Vercel preview deploys ONLY for this project:
            # e.g., https://tp-frontend-dun-git-somebranch-<team>.vercel.app
            return r"^https://tp-frontend-dun(-git-[^.]+)?\.vercel\.app$"
        else:
            # Allow private LAN hosts in dev: 10.x.x.x, 192.168.x.x, 172.16-31.x.x (any port)
            return r"^https?://(localhost|127\.0\.0\.1|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(1[6-9]|2\d|3[0-1])\.\d+\.\d+)(:\d+)?$"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
