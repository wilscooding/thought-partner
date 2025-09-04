# app/routes/health.py
from fastapi import APIRouter
import os, json
from app.infra.http import client

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/live")
async def live():
    return {"ok": True}

@router.get("/ready")
async def ready():
    return {
        "ok": True,
        "has_openrouter_key": bool(os.getenv("OPENROUTER_API_KEY")),
        "has_elevenlabs_key": bool(os.getenv("ELEVENLABS_API_KEY")),
    }

@router.get("/debug/openrouter")
async def debug_openrouter():
    key = os.getenv("OPENROUTER_API_KEY") or ""
    referer = os.getenv("OPENROUTER_HTTP_REFERER")
    title = os.getenv("OPENROUTER_X_TITLE")

    headers = {
        "Authorization": f"Bearer {key}" if key else "",
        "Content-Type": "application/json",
    }
    if referer:
        headers["HTTP-Referer"] = referer
    if title:
        headers["X-Title"] = title

    payload = {"model": "openrouter/auto", "messages": [{"role": "user", "content": "ping"}]}

    try:
        resp = await client.post_retry("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        status = resp.status_code
        text = resp.text[:200]  # trim
    except Exception as e:
        status = -1
        text = f"request failed: {e}"

    return {
        "has_key": bool(key),
        "key_prefix": key[:8] if key else None,
        "key_length": len(key) if key else 0,
        "sent_headers": {"HTTP-Referer": bool(referer), "X-Title": bool(title)},
        "upstream_status": status,
        "upstream_snippet": text,
    }
