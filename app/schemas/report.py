import datetime
from pydantic import BaseModel
from typing import Optional


class ReportBase(BaseModel):
    net_id: int
    schedule_id: Optional[int] = None
    photo_url: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None


class ReportCreate(ReportBase):
    pass


class ReportRead(ReportBase):
    id: int
    student_id: int
    verified_by: Optional[int]
    verified_at: Optional[datetime.datetime]
    created_at: datetime.datetime

    class Config:
        orm_mode = True
        from_attributes = True
