from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, Double
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class Net(Base):
    __tablename__ = "nets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)  # net_type може бути Enum
    pallete_id: Mapped[int] = mapped_column(Integer, ForeignKey("net_palletes.id"), nullable=False)
    width: Mapped[float] = mapped_column(Double, nullable=False)
    height: Mapped[float] = mapped_column(Double, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)  # net_status може бути Enum
    started_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=True)
    completed_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=True)
    final_photo_url: Mapped[str] = mapped_column(String, nullable=True)
    client_rating: Mapped[int] = mapped_column(Integer, nullable=True)
    client_comment: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)

    pallete = relationship("NetPallete", back_populates="nets")

