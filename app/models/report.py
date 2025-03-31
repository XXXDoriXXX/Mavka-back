import datetime

from sqlalchemy import Integer, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    net_id: Mapped[int] = mapped_column(ForeignKey("nets.id", ondelete="CASCADE"), nullable=False)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedules.id", ondelete="CASCADE"), nullable=True)
    verified_by: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)

    photo_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    start_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    end_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    verified_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)

    student = relationship("User", back_populates="reports", foreign_keys=[student_id])
    net = relationship("Net", back_populates="reports")
    schedule = relationship("Schedule")
    verifier = relationship("User", foreign_keys=[verified_by])