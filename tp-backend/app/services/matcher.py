from .data import avatar_descriptions, capability_descriptions, industry_experts, prompt_template

def get_avatar_profile(gender, personality_type):
  for avatar in avatar_descriptions:
    if avatar["gender"] == gender and avatar["personality_type"] == personality_type:
      return avatar
  return None


def get_capability_prompt(capability_area):
    return capability_descriptions.get(capability_area)

def get_expert_description(industry, capability_area, gender):
    for expert in industry_experts:
        if expert["industry"] == industry and expert["capability_area"] == capability_area and expert["gender"] == gender:
            return expert["expert"]
    return None

def get_prompt_template():
    return prompt_template
