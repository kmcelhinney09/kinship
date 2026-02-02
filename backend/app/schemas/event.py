from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    id:str
    family_id: str
    creator_id: str

    class Config:
        from_attributes = True