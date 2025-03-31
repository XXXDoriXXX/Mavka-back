from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True, unique=True)
    speciality_id: Mapped[int] = mapped_column(Integer, ForeignKey("specialities.id", ondelete="CASCADE"))

    speciality = relationship("Speciality", back_populates="groups")

    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    client = relationship("User", back_populates="orders")
