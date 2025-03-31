from pydantic import BaseModel
from typing import Optional, List
from app.schemas.group import GroupResponse

class SpecialityBase(BaseModel):
    name: Optional[str] = None

class SpecialityCreate(SpecialityBase):
    pass

class SpecialityResponse(SpecialityBase):
    id: int
    groups: Optional[List[GroupResponse]] = []

    class Config:
        orm_mode = True
