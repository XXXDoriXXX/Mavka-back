from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=True, unique=True)
    speciality_id: Mapped[int] = mapped_column(Integer, ForeignKey("specialities.id", ondelete="CASCADE"))

    speciality = relationship("Speciality", back_populates="groups")
    students = relationship("User", back_populates="group")
