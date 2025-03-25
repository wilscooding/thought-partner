import httpx
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# # Optional: metadata for OpenRouter rankings
# REFERER = "https://yourapp.com"
# APP_TITLE = "Thought Partner App"

def call_openrouter_api(prompt: str, model: str = "mistralai/mistral-small-3.1-24b-instruct:free") -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
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

    response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"OpenRouter API error: {response.status_code} - {response.text}")

    return response.json()["choices"][0]["message"]["content"]
