from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.user_input import UserSelection
from app.services.matcher import (
    get_avatar_profile,
    get_capability_prompt,
    get_expert_description,
    get_prompt_template
)
from app.services.data import avatar_descriptions, capability_descriptions, industry_experts
from app.services.openrouter import call_openrouter_api
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
from io import BytesIO

load_dotenv()
router = APIRouter(tags=["Match"])

# Make ElevenLabs optional in dev; guard usage inside /converse
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(api_key=elevenlabs_api_key) if elevenlabs_api_key else None


def map_voice_style_to_id(style: str) -> str:
    mapping = {
        "Warm & Expressive": "echo-rae",
        "Bold & Articulate": "indrajeet-m",
        "Elegant British": "annabel",
        # Extend or fetch dynamically
    }
    return mapping.get(style, "echo-rae")  # default fallback


@router.post("/converse")
async def converse(
    audio: UploadFile = File(...),
    gender: str = "No Preference",
    personality_type: str = "The Curious Explorer",
    capability_area: str = "Strategy & Vision",
    industry: str = "Technology"
):
    if not elevenlabs:
        raise HTTPException(status_code=503, detail="ElevenLabs is not configured on the server.")

    if not audio.content_type or not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file type")

    audio_bytes = await audio.read()
    audio_stream = BytesIO(audio_bytes)

    transcription = elevenlabs.speech_to_text.convert(
        file=audio_stream,
        model_id="scribe_v1",
        tag_audio_events=True,
        diarize=True,
    )

    user_input_text = (transcription.text or "").strip()
    if not user_input_text:
        raise HTTPException(status_code=500, detail="Transcription failed")

    user_input = UserSelection(
        gender=gender,
        personality_type=personality_type,
        capability_area=capability_area,
        industry=industry,
        user_input_text=user_input_text,
        is_first_message=True
    )

    avatar = get_avatar_profile(user_input.gender, user_input.personality_type)
    capability_prompt = get_capability_prompt(user_input.capability_area)
    expert_description = get_expert_description(user_input.industry, user_input.capability_area, user_input.gender)
    prompt_template = get_prompt_template()

    if not all([avatar, capability_prompt, expert_description, prompt_template]):
        raise HTTPException(status_code=404, detail="Incomplete mapping for one or more fields.")

    prompt = (
        prompt_template
        .replace("[INSERT INDUSTRY]", user_input.industry)
        .replace("[INSERT CAPABILITIES AREA]", capability_prompt)
        .replace("[INSERT GENDER]", user_input.gender)
        .replace("[INSERT PERSONALITY]", avatar["description"])
        .replace("[INSERT BUSINESS EXPERT]", expert_description)
        + f"\n\nHere is what the user said to begin the conversation:\n{user_input_text}"
    )

    ai_response = call_openrouter_api(prompt)

    voice_id = map_voice_style_to_id(avatar["voice_style"])
    audio_response = elevenlabs.text_to_speech(
        text=ai_response,
        voice=voice_id,
        model="eleven_multilingual_v2"
    )

    return {
        "transcript": user_input_text,
        "final_prompt": prompt,
        "ai_response": ai_response,
        "audio_url": getattr(audio_response, "url", None),
        "avatar": {
            "name": avatar["name"],
            "gender": avatar["gender"],
            "personality_type": avatar["personality_type"],
            "voice_style": avatar["voice_style"],
            "avatar_blurb": avatar.get("avatar_blurb"),
            "visual_traits": avatar.get("visual_traits"),
        },
        "expert": expert_description,
        "capability_summary": capability_prompt
    }


@router.post("/generate_prompt")
def generate_prompt(user_input: UserSelection):
    """
    Text-based matching route. Builds the system prompt and returns the AI reply and avatar metadata.
    Mirrors the logic from /converse but without audio.
    """
    avatar = get_avatar_profile(user_input.gender, user_input.personality_type)
    capability_prompt = get_capability_prompt(user_input.capability_area)
    expert_description = get_expert_description(user_input.industry, user_input.capability_area, user_input.gender)
    prompt_template = get_prompt_template()

    if not all([avatar, capability_prompt, expert_description, prompt_template]):
        raise HTTPException(status_code=404, detail="Incomplete mapping for one or more fields.")

    if user_input.is_first_message:
        prompt = (
            prompt_template
            .replace("[INSERT INDUSTRY]", user_input.industry)
            .replace("[INSERT CAPABILITIES AREA]", capability_prompt)
            .replace("[INSERT GENDER]", user_input.gender)
            .replace("[INSERT PERSONALITY]", avatar["description"])
            .replace("[INSERT BUSINESS EXPERT]", expert_description)
        )
        prompt += f"\n\nHere is what the user said to begin the conversation:\n{user_input.user_input_text}"
    else:
        # Continue the conversation with the raw user input
        prompt = user_input.user_input_text

    ai_response = call_openrouter_api(prompt)

    return {
        "final_prompt": prompt,
        "ai_response": ai_response,
        "avatar": {
            "name": avatar["name"],
            "gender": avatar["gender"],
            "personality_type": avatar["personality_type"],
            "voice_style": avatar["voice_style"],
            "avatar_blurb": avatar.get("avatar_blurb"),
            "visual_traits": avatar.get("visual_traits"),
        },
        "expert": expert_description,
        "capability_summary": capability_prompt
    }


@router.get("/options")
def get_user_selection_options():
    industries = [
        {"label": industry, "value": industry}
        for industry in sorted(set(expert["industry"] for expert in industry_experts))
    ]

    capability_area_labels = {
        "Customer Experience": "Customer Experience – Journey mapping, feedback, and loyalty",
        "Finance": "Finance – Budgets, funding, pricing, and financial strategy",
        "Marketing & Sales": "Marketing & Sales – Reaching customers and driving growth",
        "Operations": "Operations – Day-to-day structure, efficiency, and systems",
        "People & Culture": "People & Culture – Hiring, leadership, team dynamics",
        "Product & Innovation": "Product & Innovation – Building and improving your offering",
        "Risk & Compliance": "Risk & Compliance – Legal, ethical, and operational safeguards",
        "Strategy & Vision": "Strategy & Vision – Big picture thinking, long-term goals, and direction",
        "Sustainability & Social Impact": "Sustainability & Social Impact – Doing good while doing business",
        "Technology & Data": "Technology & Data – Tech tools, automation, and data insights",
    }

    capability_areas = [
        {"label": label, "value": key}
        for key, label in capability_area_labels.items()
    ]

    personality_labels = {
        "The Adaptive Chameleon": "Someone flexible who can meet me wherever I’m at today",
        "The Analytical Architect": "Someone analytical who can help me think through complex ideas",
        "The Bold Provocateur": "Someone direct who’ll challenge my thinking (in a good way)",
        "The Curious Explorer": "Someone curious and energetic who helps me explore new possibilities",
        "The Empathetic Listener": "Someone supportive who really listens and gets where I’m coming from",
        "The Grounded Realist": "Someone practical who keeps things clear and grounded",
        "The Humble Sage": "Someone wise and calm who helps me reflect and grow",
        "The Quiet Catalyst": "Someone thoughtful who helps me see things differently, without pushing",
        "The Strategic Optimist": "Someone hopeful and future-focused who helps me see what’s possible"
    }

    personality_types = [
        {"label": label, "value": key}
        for key, label in personality_labels.items()
    ]

    gender_labels = {
        "Woman": "Woman",
        "Man": "Man",
        "Non-Binary": "Non-Binary",
        "No Preference": "No Preference"
    }

    genders = [
        {"label": label, "value": key}
        for key, label in gender_labels.items()
    ]

    return {
        "industry": {
            "question": "What industry are you working in or thinking about today?",
            "options": industries
        },
        "capability_area": {
            "question": "What kind of guidance are you looking for today?",
            "options": capability_areas
        },
        "personality_type": {
            "question": "What type of personality would be most helpful for you to talk to today?",
            "options": personality_types
        },
        "gender": {
            "question": "Do you have a gender you’d feel most comfortable talking to?",
            "options": genders
        }
    }


# Create a mapping from slug to avatar
slug_to_avatar = {
    avatar["name"].lower().replace(" ", "-"): avatar for avatar in avatar_descriptions
}

@router.get("/tp-profiles")
def get_all_thought_partners():
    return list(slug_to_avatar.values())
