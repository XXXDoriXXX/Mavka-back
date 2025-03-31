from pydantic import BaseModel, Field
from typing import Optional
from app.models.user import UserRole

class UserSignup(BaseModel):
    username: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = UserRole.STUDENT

    class Config:
        orm_mode = True
