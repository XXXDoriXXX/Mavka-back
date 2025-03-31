import datetime

from sqlalchemy import Integer, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base
from enum import Enum as PyEnum


class OrderStatus(PyEnum):
    PENDING = "pending"
    CONFIRMATION = "confirmation"
    COMPLETED = "completed"
    CANCELED = "canceled"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), nullable=False)

    deadline: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    started_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    completed_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False)

    client = relationship("User", back_populates="orders")
    nets = relationship("Net", back_populates="order")