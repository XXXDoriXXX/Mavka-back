from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum
from app.schemas.net_pallete import NetPalleteResponse


class NetStatus(str, Enum):
    PLANNED = "planned"
    WORKING = "working"
    CONFIRMATION = "confirmation"
    COMPLETED = "completed"
    CANCELED = "canceled"


class NetType(str, Enum):
    RIBBON = "ribbon"
    BOW = "bow"


class NetBase(BaseModel):
    order_id: int
    type: NetType
    width: float
    height: float
    status: NetStatus
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    final_photo_url: Optional[str] = None
    client_rating: Optional[int] = None
    client_comment: Optional[str] = None
    created_at: datetime

    class Config:
        use_enum_values = True


class NetCreate(NetBase):
    pallete_id: int
    pass


class NetResponse(NetBase):
    id: int
    pallete_id: int

    class Config:
        orm_mode = True
        from_attributes = True


class NetResponseFull(NetBase):
    id: int
    pallete: NetPalleteResponse

    class Config:
        orm_mode = True
        from_attributes = True