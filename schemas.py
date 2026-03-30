from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class DamageReportBase(BaseModel):
    latitude: float
    longitude: float
    damage_level: str
    notes: Optional[str] = None

class DamageReportCreate(DamageReportBase):
    # reporter_id and image_url are handled by services, 
    # so they aren't required in the initial Pydantic check from the form
    pass

class DamageReportResponse(DamageReportBase):
    id: int
    public_lat: float
    public_lng: float
    image_url: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
