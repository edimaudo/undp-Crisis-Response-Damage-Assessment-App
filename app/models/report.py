from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    damage_level = Column(String)
    image_url = Column(String)
    hash = Column(String)
    is_duplicate = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
