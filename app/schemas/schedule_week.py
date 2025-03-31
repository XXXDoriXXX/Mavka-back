import datetime
from pydantic import BaseModel
from typing import Optional


class ScheduleWeekBase(BaseModel):
    start_date: datetime.date
    specialty_id: int
    notes: Optional[str] = None


class ScheduleWeekCreate(ScheduleWeekBase):
    pass


class ScheduleWeekRead(ScheduleWeekBase):
    id: int
    end_date: datetime.date

    class Config:
        orm_mode = True
