from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.db.session import SessionLocal
from app.services.report_service import create_report

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/submit")
def submit(
    file: UploadFile = File(...),
    lat: float = Form(...),
    lon: float = Form(...),
    db=Depends(get_db)
):
    return create_report(db, file.file, lat, lon)
