from enum import Enum
from typing import List
from pydantic import BaseModel, Field, constr, validator
from app.services.data import industry_experts

class CapabilityArea(str, Enum):
  customer_experience = "Customer Experience"
  finance = "Finance"
  marketing_sales = "Marketing & Sales"
  operations = "Operations"
  people_culture = "People & Culture"
  product_innovation = "Product & Innovation"
  risk_compliance = "Risk & Compliance"
  strategy_vision = "Strategy & Vision"
  sustainability_social_impact = "Sustainability & Social Impact"
  technology_data = "Technology & Data"


# --- Personality types (must match /options keys exactly) ---
class PersonalityType(str, Enum):
    adaptive_chameleon = "The Adaptive Chameleon"
    analytical_architect = "The Analytical Architect"
    bold_provocateur = "The Bold Provocateur"
    curious_explorer = "The Curious Explorer"
    empathetic_listener = "The Empathetic Listener"
    grounded_realist = "The Grounded Realist"
    humble_sage = "The Humble Sage"
    quiet_catalyst = "The Quiet Catalyst"
    strategic_optimist = "The Strategic Optimist"

# --- Genders (must match /options keys exactly) ---
class Gender(str, Enum):
    woman = "Woman"
    man = "Man"
    non_binary = "Non-Binary"
    no_preference = "No Preference"

UserText = constr(min_length=1, max_length=1000)

def _allowed_industries() -> List[str]:
   return sorted({expert["industry"] for expert in industry_experts})


class UserSelection(BaseModel):
  industry: str = Field(..., description="Select Industry (from /api/options)")
  capability_area: str = Field(..., description="Select Capability Area (from /api/options)")
  personality_type: str = Field(..., description="Select Personality Type (from /api/options)")
  gender: str = Field(..., description="Select Gender (from /api/options)")
  user_input_text: UserText
  is_first_message: bool = True
  # is_first_message: Optional[bool] = True

  @validator("industry")
  def industry_must_be_valid(cls, v: str) -> str:
      if v not in _allowed_industries():
          allowed =  ", ".join(_allowed_industries())
          raise ValueError(f"Industry must be one of: {allowed}")
      return v
