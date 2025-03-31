import datetime
from pydantic import BaseModel
from typing import Optional, List


class ScheduleBase(BaseModel):
    date: datetime.date
    template_id: int
    teacher_id: Optional[int] = None
    group_ids: List[int]
    is_cleaning: bool = False


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleRead(ScheduleBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True