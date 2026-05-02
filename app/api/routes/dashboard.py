from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from app.services.analytics_service import get_stats

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/data")
def data(db=Depends(get_db)):
    return get_stats(db)
