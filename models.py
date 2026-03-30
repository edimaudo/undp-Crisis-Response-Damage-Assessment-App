from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text
from sqlalchemy.sql import func
from .database import Base


class DamageReport(Base):
    __tablename__ = "damage_reports"

    id = Column(Integer, primary_key=True, index=True)
    
    # 1. Precise Location (Internal UNDP use only)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    # 2. Public/Fuzzed Location (For the Community Map)
    # Calculated via PrivacyService before saving
    public_lat = Column(Float, index=True)
    public_lng = Column(Float, index=True)

    # 3. Assessment Data
    damage_level = Column(String, nullable=False) # minor, major, destroyed
    
    # 4. Media & Evidence
    # We store the file path/URL, not the actual file bytes
    image_url = Column(String, nullable=True) 
    
    # 5. Optional Context (Combined notes for speed)
    notes = Column(Text, nullable=True) 
    
    # 6. Metadata
    reporter_id = Column(String, nullable=True) # Anonymized hash
    created_at = Column(DateTime(timezone=True), server_default=func.now())
