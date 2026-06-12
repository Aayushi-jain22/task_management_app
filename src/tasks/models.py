from sqlalchemy import Column, Integer, String, Text, DateTime
from src.utils.db import Base ## base is repsnsble to connect tables

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Integer, nullable=False, default=False)
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)