from fastapi import APIRouter, HTTPException
from app.models.user_input import UserSelection
from app.services.matcher import (
    get_avatar_description,
    get_capability_prompt,
    get_expert_description,
    get_prompt_template
)
from app.services.data import avatar_descriptions, capability_descriptions, industry_experts
from app.services.openrouter import call_openrouter_api

router = APIRouter()

@router.post("/generate_prompt")
def generate_prompt(user_input: UserSelection):
    personality_prompt = get_avatar_description(user_input.gender, user_input.personality_type)
    capability_prompt = get_capability_prompt(user_input.capability_area)
    expert_description = get_expert_description(user_input.industry, user_input.capability_area, user_input.gender)
    prompt_template = get_prompt_template()


    if not all([personality_prompt, capability_prompt, expert_description]):
        raise HTTPException(status_code=404, detail="Incomplete mapping for one or more fields.")

    if user_input.is_first_message:
      prompt = prompt_template
      prompt = prompt.replace("[INSERT INDUSTRY]", user_input.industry)
      prompt = prompt.replace("[INSERT CAPABILITIES AREA]", capability_prompt)
      prompt = prompt.replace("[INSERT GENDER]", user_input.gender)
      prompt = prompt.replace("[INSERT PERSONALITY]", personality_prompt)
      prompt = prompt.replace("[INSERT BUSINESS EXPERT]", expert_description)

      prompt += f"\n\nHere is what the user said to begin the conversation:\n{user_input.user_input_text}"
    else:
      prompt = user_input.user_input_text

    ai_response = call_openrouter_api(prompt)

    return {"final_prompt": prompt, "ai_response": ai_response}

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
