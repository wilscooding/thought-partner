import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()



OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("DEBUG: OPENROUTER_API_KEY loaded as:", OPENROUTER_API_KEY)
# Optional metadata
# REFERER = "https://yourapp.com"
# APP_TITLE = "Thought Partner App"

async def call_openrouter_api(
    prompt: str,
    model: str = "mistralai/mistral-small-3.1-24b-instruct:free"
) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # "HTTP-Referer": REFERER,
        # "X-Title": APP_TITLE
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful and strategic thought partner."},
            {"role": "user", "content": prompt}
        ]
    }

    timeout = httpx.Timeout(15.0)

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(url, headers=headers, json=payload)

        response.raise_for_status()

        data = response.json()
        choices = data.get("choices", [])
        if not choices or "message" not in choices[0]:
            raise HTTPException(status_code=502, detail="OpenRouter response malformed.")

        return choices[0]["message"]["content"]

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"OpenRouter HTTP error: {e.response.text}")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="OpenRouter API timed out.")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"OpenRouter request failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected OpenRouter error: {str(e)}")
