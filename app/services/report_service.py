from app.models.report import Report
from app.services.image_duplicate_service import compute_hash, is_duplicate
from app.services.ai_classification import classify_damage

def create_report(db, file, lat, lon):
    hash_val = compute_hash(file)

    existing = [r.hash for r in db.query(Report).all()]
    dup = is_duplicate(hash_val, existing)

    damage = classify_damage({})

    report = Report(
        latitude=lat,
        longitude=lon,
        damage_level=damage,
        hash=hash_val,
        is_duplicate=dup
    )

    db.add(report)
    db.commit()
    return report
