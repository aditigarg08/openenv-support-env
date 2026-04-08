from pydantic import BaseModel
from typing import List, Optional

class Ticket(BaseModel):
    id: int
    text: str
    priority: str  # low, medium, high

class Observation(BaseModel):
    tickets: List[Ticket]
    last_action: Optional[str]

class Action(BaseModel):
    action_type: str  # "classify"
    ticket_id: int
    predicted_priority: str

class Reward(BaseModel):
    score: float