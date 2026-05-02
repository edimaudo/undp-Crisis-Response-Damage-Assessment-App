def to_geojson(reports):
    return {
        "type":"FeatureCollection",
        "features":[
            {
                "type":"Feature",
                "geometry":{"type":"Point","coordinates":[r.longitude,r.latitude]},
                "properties":{"damage":r.damage_level}
            } for r in reports
        ]
    }
