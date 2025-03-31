from sqlalchemy import Integer, ForeignKey, Table, Column
from app.db.session import Base

schedule_group = Table(
    "schedule_group",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
    Column("schedule_id", Integer, ForeignKey("schedules.id"), primary_key=True),
)
