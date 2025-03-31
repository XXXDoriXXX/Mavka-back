from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    name: Optional[str] = None
    speciality_id: int

class GroupCreate(GroupBase):
    pass

class GroupResponse(GroupBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
