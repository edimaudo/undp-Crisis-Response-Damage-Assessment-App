from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from app.models.report import Report
from app.services.export_service import to_geojson

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/geojson")
def geojson(db=Depends(get_db)):
    return to_geojson(db.query(Report).all())
