from pydantic import BaseModel
from typing import Optional

class NetPalleteBase(BaseModel):
    name: str
    example_url: Optional[str] = None
    desc: Optional[str] = None

class NetPalleteCreate(NetPalleteBase):
    pass

class NetPalleteResponse(NetPalleteBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
