from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Dict

class DamageReportBase(BaseModel):
    latitude: float
    longitude: float
    damage_level: str
    reporter_name: Optional[str] = None
    needs_assessment: Optional[Dict[str, bool]] = None

class DamageReportCreate(DamageReportBase):
    pass

class DamageReportResponse(DamageReportBase):
    id: int
    created_at: datetime
    
    # Modern Pydantic V2 config for SQLAlchemy compatibility
    model_config = ConfigDict(from_attributes=True)
