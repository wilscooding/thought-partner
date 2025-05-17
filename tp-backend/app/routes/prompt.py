from fastapi import APIRouter, HTTPException
from app.models.user_input import UserSelection
from app.services.matcher import (
    get_avatar_profile,
    get_capability_prompt,
    get_expert_description,
    get_prompt_template
)
from app.services.data import avatar_descriptions, capability_descriptions, industry_experts
from app.services.openrouter import call_openrouter_api

router = APIRouter()

@router.post("/generate_prompt")
def generate_prompt(user_input: UserSelection):
    # personality_prompt = get_avatar_description(user_input.gender, user_input.personality_type)
    avatar = get_avatar_profile(user_input.gender, user_input.personality_type)
    capability_prompt = get_capability_prompt(user_input.capability_area)
    expert_description = get_expert_description(user_input.industry, user_input.capability_area, user_input.gender)
    prompt_template = get_prompt_template()

       # Print out values for debugging
    print("DEBUG: Avatar:", avatar)
    print("Available capability areas:", list(capability_descriptions.keys()))
    print("Available industry+capability+gender:", [
    (e["industry"], e["capability_area"], e["gender"]) for e in industry_experts
])

    print("DEBUG: Capability Prompt:", capability_prompt)
    print("DEBUG: Expert Description:", expert_description)


    if not all([avatar, capability_prompt, expert_description]):
        raise HTTPException(status_code=404, detail="Incomplete mapping for one or more fields.")

    if user_input.is_first_message:
      prompt = prompt_template
      prompt = prompt.replace("[INSERT INDUSTRY]", user_input.industry)
      prompt = prompt.replace("[INSERT CAPABILITIES AREA]", capability_prompt)
      prompt = prompt.replace("[INSERT GENDER]", user_input.gender)
      prompt = prompt.replace("[INSERT PERSONALITY]", avatar["description"])
      prompt = prompt.replace("[INSERT BUSINESS EXPERT]", expert_description)

      prompt += f"\n\nHere is what the user said to begin the conversation:\n{user_input.user_input_text}"
    else:
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
    industries = sorted(set(expert["industry"] for expert in industry_experts))
    capability_areas = sorted(capability_descriptions.keys())
    genders = sorted(set(avatar["gender"] for avatar in avatar_descriptions))
    personality_types = sorted(set(avatar["personality_type"] for avatar in avatar_descriptions))

    return {
        "industries": industries,
        "capability_areas": capability_areas,
        "genders": genders,
        "personality_types": personality_types
    }


# Create a mapping from slug to avatar
slug_to_avatar = {
    avatar["name"].lower().replace(" ", "-"): avatar for avatar in avatar_descriptions
}

@router.get("/tp-profiles")
def get_all_thought_partners():
    return list(slug_to_avatar.values())

@router.get("/tp-profiles/{slug}")
def get_thought_partner_by_slug(slug: str):
    if slug not in slug_to_avatar:
        raise HTTPException(status_code=404, detail="Thought Partner not found")
    return slug_to_avatar[slug]
