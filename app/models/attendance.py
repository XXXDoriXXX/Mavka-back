from sqlalchemy import Integer, String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base
from enum import Enum as PyEnum


class AttendanceStatus(PyEnum):
    PRESENT = "present"
    ABSENT = "absent"
    EXCUSED = "excused"


class Attendance(Base):
    __tablename__ = "attendances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedules.id"), nullable=False)
    status: Mapped[AttendanceStatus] = mapped_column(Enum(AttendanceStatus), nullable=True)
    notes: Mapped[str] = mapped_column(String, nullable=True)

    student = relationship("User")
    schedule = relationship("Schedule")
