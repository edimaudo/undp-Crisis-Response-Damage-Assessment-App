import json
from typing import List
from ..models import DamageReport

class ExportService:
    @staticmethod
    def generate_geojson(reports: List[DamageReport]) -> str:
        features = []
        for r in reports:
            features.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [r.longitude, r.latitude]},
                "properties": {
                    "severity": r.damage_level,
                    "id": r.id
                }
            })
        return json.dumps({"type": "FeatureCollection", "features": features})
