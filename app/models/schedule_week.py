import datetime

from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class ScheduleWeek(Base):
    __tablename__ = "schedule_weeks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False, unique=True)
    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"), nullable=False)
    notes: Mapped[str] = mapped_column(String, nullable=True)

    specialty = relationship("Speciality", back_populates="weeks")
    schedules = relationship("Schedule", back_populates="week")

    @property
    def end_date(self) -> datetime.date:
        return self.start_date + datetime.timedelta(days=6)
