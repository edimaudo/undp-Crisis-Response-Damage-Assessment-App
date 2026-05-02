from sqlalchemy import func
from app.models.report import Report

def get_stats(db):
    total = db.query(func.count(Report.id)).scalar()
    return {"total": total}
