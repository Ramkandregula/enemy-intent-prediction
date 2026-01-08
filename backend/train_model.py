from fastapi import FastAPI
import joblib
from database import conn, cursor

app = FastAPI()

threat_model = joblib.load("threat_model.pkl")

@app.post("/detect-threat")
def detect_threat():

    cursor.execute("""
        SELECT speed, distance, direction, hospitality, latitude, longitude
        FROM satellite_data
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    if not row:
        return {"error": "No satellite data available"}

    speed, distance, direction, hospitality, lat, lon = row

    features = [[speed, distance, direction, hospitality]]
    threat = int(threat_model.predict(features)[0])

    threat_map = {0: "LOW", 1: "MEDIUM", 2: "HIGH"}

    explanation_map = {
        0: "Low speed and safe distance indicates normal movement",
        1: "Moderate speed and distance indicates suspicious activity",
        2: "High speed near sensitive zone indicates hostile intent"
    }

    return {
        "threat_level": threat_map[threat],
        "explanation": explanation_map[threat],
        "used_data": {
            "speed": speed,
            "distance": distance,
            "direction": direction,
            "hospitality": hospitality,
            "latitude": lat,
            "longitude": lon
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)