import json
from typing import List
from ..models import DamageReport

class ExportEngine:
    @staticmethod
    def to_geojson(reports: List[DamageReport]) -> dict:
        """
        Converts a list of DB reports into a standard GeoJSON FeatureCollection.
        Reasoning: This is the native format for the Community Map.
        """
        features = []
        for report in reports:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [report.longitude, report.latitude]
                },
                "properties": {
                    "id": report.id,
                    "severity": report.damage_level,
                    "timestamp": report.created_at.isoformat() if report.created_at else None,
                    "image_url": report.image_url
                }
            }
            features.append(feature)
            
        return {
            "type": "FeatureCollection",
            "features": features
        }

    @staticmethod
    def to_csv_ready_list(reports: List[DamageReport]) -> List[dict]:
        """
        Flattens data for CSV export.
        Reasoning: Field officers often need Excel-compatible data for 
        logistics planning.
        """
        return [
            {
                "Report_ID": r.id,
                "Lat": r.latitude,
                "Lon": r.longitude,
                "Severity": r.damage_level,
                "Date": r.created_at
            } for r in reports
        ]
