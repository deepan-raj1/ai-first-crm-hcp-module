from datetime import date, time, datetime
from typing import Optional

from pydantic import BaseModel


# ----------------------------
# Base Schema
# ----------------------------

class InteractionBase(BaseModel):
    hcp_name: str
    interaction_type: str

    date: date
    time: time

    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None

    sentiment: Optional[str] = None

    outcome: Optional[str] = None
    follow_up_actions: Optional[str] = None

    summary: Optional[str] = None


# ----------------------------
# Create Schema
# ----------------------------

class InteractionCreate(InteractionBase):
    pass


# ----------------------------
# Update Schema
# ----------------------------

class InteractionUpdate(BaseModel):
    hcp_name: Optional[str] = None
    interaction_type: Optional[str] = None

    date: Optional[date] = None
    time: Optional[time] = None

    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None

    sentiment: Optional[str] = None

    outcome: Optional[str] = None
    follow_up_actions: Optional[str] = None

    summary: Optional[str] = None

# ----------------------------
# Response Schema
# ----------------------------

class InteractionResponse(InteractionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True