from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from .database import Base

class DamageReport(Base):
    __tablename__ = "damage_reports"

    id = Column(Integer, primary_key=True, index=True)
    reporter_name = Column(String, nullable=True)
    # Essential for the Community Map
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # Crisis specific data
    damage_level = Column(String, nullable=False) # e.g., Minor, Significant, Destroyed
    needs_assessment = Column(JSON, nullable=True) # e.g., {"water": True, "medical": False}
    created_at = Column(DateTime(timezone=True), server_default=func.now())
