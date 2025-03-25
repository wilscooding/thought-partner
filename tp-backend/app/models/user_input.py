from pydantic import BaseModel
from typing import Optional


class UserSelection(BaseModel):
  industry: str
  capability_area: str
  gender: str
  personality_type: str
  user_input_text: str
  is_first_message: Optional[bool] = True
