from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


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
    pallete_id: int
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
    pass


class NetResponse(NetBase):
    id: int

    class Config:
        orm_mode = True
