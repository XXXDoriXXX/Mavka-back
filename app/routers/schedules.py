from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.schedule_week import ScheduleWeek
from app.models.schedule import Schedule
from app.schemas.schedule_week import ScheduleWeekCreate, ScheduleWeekRead
from app.schemas.schedule import ScheduleCreate, ScheduleRead
from app.dependencies import require_role

import datetime

router = APIRouter(prefix="/schedule", tags=["schedule"])


@router.get("/weeks/", response_model=List[ScheduleWeekRead])
def list_weeks(
        speciality_id: int,
        db: Session = Depends(get_db)
):
    return db.query(ScheduleWeek).filter(ScheduleWeek.speciality_id == speciality_id).order_by(
        ScheduleWeek.start_date).all()


@router.post("/weeks/", response_model=ScheduleWeekRead)
def create_week(data: ScheduleWeekCreate,
                db: Session = Depends(get_db),
                current_user = Depends(require_role("teacher"))):
    week = ScheduleWeek(**data.dict())
    db.add(week)
    db.commit()
    db.refresh(week)
    return week


@router.get("/weeks/{week_id}/schedule", response_model=List[ScheduleRead])
def get_week_schedule(
        week_id: int,
        db: Session = Depends(get_db)):
    schedules = db.query(Schedule).filter(Schedule.week_id == week_id).order_by(
        Schedule.date).all()
    return schedules


@router.post("/weeks/{week_id}/schedule", response_model=List[ScheduleRead])
def create_or_replace_schedule(
        week_id: int,
        data: List[ScheduleCreate],
        db: Session = Depends(get_db),
        current_user=Depends(require_role("teacher")),
):
    db.query(Schedule).filter(Schedule.week_id == week_id).delete()

    result = []
    for entry in data:
        schedule = Schedule(**entry.dict(), week_id=week_id)
        db.add(schedule)
        db.flush()

        for group_id in entry.group_ids:
            db.execute(
                "INSERT INTO schedule_group (group_id, schedule_id) VALUES (:group_id, :schedule_id)",
                {"group_id": group_id, "schedule_id": schedule.id}
            )
        result.append(schedule)

    db.commit()
    return result
