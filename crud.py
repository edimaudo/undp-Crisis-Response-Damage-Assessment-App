from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_damage_report(db: AsyncSession, report: schemas.DamageReportCreate):
    db_report = models.DamageReport(**report.model_dump())
    db.add(db_report)
    await db.commit()
    await db.refresh(db_report)
    return db_report

async def get_all_reports(db: AsyncSession):
    result = await db.execute(select(models.DamageReport))
    return result.scalars().all()
