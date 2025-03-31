from pydantic import BaseModel
from typing import Optional, List
from app.schemas.net import NetResponse

class OrderBase(BaseModel):
    name: Optional[str] = None
    speciality_id: int
    client_id: int

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    nets: Optional[List[NetResponse]] = []

    class Config:
        orm_mode = True
