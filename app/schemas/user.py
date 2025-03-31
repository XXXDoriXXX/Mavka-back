from pydantic import BaseModel, Field
from typing import Optional
from app.models.user import UserRole

class UserSignup(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    group_id: int

    role: UserRole = UserRole.STUDENT

    class Config:
        orm_mode = True
        from_attributes = True
