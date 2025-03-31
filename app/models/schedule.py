import datetime

from sqlalchemy import Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    template_id: Mapped[int] = mapped_column(ForeignKey("schedule_templates.id"), nullable=False)
    week_id: Mapped[int] = mapped_column(ForeignKey("schedule_weeks.id"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    is_cleaning: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    template = relationship("ScheduleTemplate", back_populates="schedules")
    week = relationship("ScheduleWeek", back_populates="schedules")
    teacher = relationship("User")
    groups = relationship("Group", secondary="schedule_group")
