from fastapi import FastAPI
from datetime import datetime
from backend.model import predict_enemy_intent

app = FastAPI()

def generate_inputs():
    now = datetime.now()

    # 🔥 FORCE HIGH THREAT SOMETIMES (DEMO SAFE)
    if now.second % 3 == 0:
        speed = 95
        distance = 12
    else:
        speed = (now.second * 2) % 120
        distance = (90 - now.second) % 100

    direction = (now.minute * 6) % 360
    hospitality = round((now.second % 10) / 10, 2)
    latitude = 28.6
    longitude = 77.2

    return speed, distance, direction, hospitality, latitude, longitude

@app.get("/detect-threat")
def detect_threat():
    speed, distance, direction, hospitality, lat, lon = generate_inputs()

    ai = predict_enemy_intent(
        [speed, distance, direction, hospitality]
    )

    return {
        **ai,
        "inputs": {
            "speed": speed,
            "distance": distance,
            "direction": direction,
            "hospitality": hospitality,
            "latitude": lat,
            "longitude": lon
        }
    }
