from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

class NetPallete(Base):
    __tablename__ = "net_palletes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    example_url: Mapped[str] = mapped_column(String, nullable=True)
    desc: Mapped[str] = mapped_column(String, nullable=True)

    nets = relationship("Net", back_populates="pallete")