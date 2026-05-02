import numpy as np

def predict_damage_trend(reports):
    """
    Simple baseline:
    - Uses time-series frequency of reports
    - Outputs projected counts
    """

    if not reports:
        return {"forecast": []}

    counts = [r["count"] for r in reports]

    trend = np.polyfit(range(len(counts)), counts, 1)
    forecast = [int(trend[0]*i + trend[1]) for i in range(len(counts), len(counts)+5)]

    return {"forecast": forecast}
