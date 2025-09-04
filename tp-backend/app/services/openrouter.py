import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from app.infra.http import client

load_dotenv()



OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openrouter/auto"

# Optional metadata
# REFERER = "https://yourapp.com"
# APP_TITLE = "Thought Partner App"

def _get_api_key() -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OpenRouter API key not configured.")
    return api_key

async def call_openrouter_api(
    prompt: str,
    model: str = DEFAULT_MODEL,
    system_prompt: str = "You are a helpful and strategic thought partner.",
) -> str:
    
    headers = {
        "Authorization": f"Bearer {_get_api_key()}",
        "Content-Type": "application/json",
        # "HTTP-Referer": REFERER,
        # "X-Title": APP_TITLE
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    }



    try:
        response = await client.post_retry(OPENROUTER_URL, headers=headers, json=payload)
        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=f"OpenRouter HTTP error: {response.text}")
        
        data = response.json()
        choices = data.get("choices", [])
        if not choices or "message" not in choices[0]:
            raise HTTPException(status_code=502, detail="OpenRouter response malformed.")

        return choices[0]["message"]["content"]
    
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="OpenRouter API timed out")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"OpenRouter HTTP error: {e.response.text}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"OpenRouter request failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected OpenRouter error: {str(e)}")
