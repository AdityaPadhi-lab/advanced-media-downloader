from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    source_url: str
    chat_id: Optional[int]
    msg_id: Optional[int]

class TaskOut(BaseModel):
    id: int
    source_url: str
    status: str
    class Config:
        orm_mode = True
