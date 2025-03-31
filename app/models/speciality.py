from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

class Speciality(Base):
    __tablename__ = 'specialities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=True, unique=True)

    groups = relationship("Group", back_populates="speciality", cascade="all, delete")
