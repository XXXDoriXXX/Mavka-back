from pydantic import BaseModel
from typing import Optional, List
from app.schemas.net import NetResponse

class NetPalleteBase(BaseModel):
    name: str
    example_url: Optional[str] = None
    desc: Optional[str] = None

class NetPalleteCreate(NetPalleteBase):
    pass

class NetPalleteResponse(NetPalleteBase):
    id: int
    nets: Optional[List[NetResponse]] = []

    class Config:
        orm_mode = True
