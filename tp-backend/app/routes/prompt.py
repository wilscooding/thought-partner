from fastapi import APIRouter, HTTPException, UploadFile, File, Request
from app.models.user_input import UserSelection
from app.services.matcher import (
    get_avatar_profile,
    get_capability_prompt,
    get_expert_description,
    get_prompt_template
)
from app.services.data import avatar_descriptions, capability_descriptions, industry_experts
from app.services.openrouter import call_openrouter_api
from dotenv import load_dotenv
import os
from io import BytesIO
import logging

load_dotenv()
router = APIRouter(tags=["Match"])


def map_voice_style_to_id(style: str) -> str:
    mapping = {
        "Warm & Expressive": "echo-rae",
        "Bold & Articulate": "indrajeet-m",
        "Elegant British": "annabel",
        # Extend or fetch dynamically
    }
    return mapping.get(style, "echo-rae")  # default fallback




@router.post("/generate_prompt")
async def generate_prompt(user_input: UserSelection, request: Request):
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

    try:
        ai_response = await call_openrouter_api(prompt, model="openrouter/auto")
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.getLogger(__name__).exception("Error calling OpenRouter API")
        raise HTTPException(status_code=500, detail="Internal error calling AI service.")

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

@router.get("/tp-profiles/{slug}")
def get_thought_partner(slug: str):
    avatar = slug_to_avatar.get(slug)
    if not avatar:
        raise HTTPException(status_code=404, detail="Thought partner not found")
    return avatar

