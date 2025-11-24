from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    source_url = Column(Text, nullable=False)
    status = Column(String(32), default="pending")
    result_path = Column(Text, nullable=True)
    checksum = Column(String(128), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
