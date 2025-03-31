from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from app.config import appConfig

DATABASE_URL = appConfig.database.database_connection_string

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
