from sqlalchemy import Column, Integer, String, Enum, DateTime
import enum
import datetime
from app.db.session import Base

class UserRole(enum.Enum):
    ADMIN = "admin"
    CLIENT = "client"
    TEACHER = "teacher"
    STUDENT = "student"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
