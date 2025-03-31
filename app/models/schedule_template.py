import datetime

from sqlalchemy import Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class ScheduleTemplate(Base):
    __tablename__ = "schedule_templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    end_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)

    schedules = relationship("Schedule", back_populates="template")
