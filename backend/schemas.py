from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AgentCreate(BaseModel):
    name: str
    provider: str
    model: str
    api_key: str
    base_url: Optional[str] = None
    system_prompt: Optional[str] = None
    temperature: float = 0.7
    avatar_color: str = "#6366f1"
    order_index: int = 0

class RoomCreate(BaseModel):
    name: str
    topic: str
    agents: List[AgentCreate]

class RoomOut(BaseModel):
    id: int
    name: str
    topic: str
    status: str
    created_at: datetime
    model_config = {"from_attributes": True}

class MessageOut(BaseModel):
    id: int
    agent_name: str
    content: str
    round_num: int
    created_at: datetime
    agent_id: Optional[int]
    model_config = {"from_attributes": True}

class ConferenceStart(BaseModel):
    rounds: int = 3
    moderator_prompt: Optional[str] = None

































