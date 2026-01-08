from fastapi import FastAPI
import joblib
from pathlib import Path
from datetime import datetime

# ✅ Database import
from backend.database import conn, cursor

# ✅ Explanation engine import
from backend.explanation import explanation_engine

# =============================
# App initialization
# =============================
app = FastAPI(
    title="Enemy Intent Prediction API",
    version="1.0"
)

# =============================
# Load ML model safely
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "threat_model.pkl"

if not MODEL_PATH.exists():
    raise RuntimeError(
        f"Model file not found at {MODEL_PATH}. "
        f"Run train_model.py first."
    )

threat_model = joblib.load(MODEL_PATH)

# =============================
# Time-based input generator
# (NO random used)
# =============================
def generate_time_based_inputs():
    now = datetime.now()

    speed = (now.second * 2) % 120          # 0–120
    distance = (60 - now.second) % 100      # 0–100
    direction = (now.minute * 6) % 360      # 0–360
    hospitality = (now.second % 10) / 10.0  # 0.0–0.9

    latitude = 28.6 + (now.minute % 5) * 0.1
    longitude = 77.2 + (now.second % 5) * 0.1

    return speed, distance, direction, hospitality, latitude, longitude

# =============================
# Health check
# =============================
@app.get("/")
def root():
    return {"status": "Backend is running"}

# =============================
# Threat detection endpoint
# =============================
@app.post("/detect-threat")
def detect_threat():

    # 🔹 Generate time-based satellite inputs
    speed, distance, direction, hospitality, lat, lon = generate_time_based_inputs()

    # 🔹 Store data (time-series intelligence)
    cursor.execute("""
        INSERT INTO satellite_data
        (speed, distance, direction, hospitality, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (speed, distance, direction, hospitality, lat, lon))
    conn.commit()

    # 🔹 ML Prediction
    features = [[speed, distance, direction, hospitality]]
    threat = int(threat_model.predict(features)[0])

    threat_map = {
        0: "LOW",
        1: "MEDIUM",
        2: "HIGH"
    }

    # 🔹 AI Explanation
    explanation = explanation_engine(
        speed, distance, direction, hospitality
    )

    return {
        "timestamp": datetime.now().isoformat(),
        "threat_level": threat_map[threat],
        "explanation": explanation,
        "used_data": {
            "speed": round(speed, 2),
            "distance": round(distance, 2),
            "direction": round(direction, 2),
            "hospitality": round(hospitality, 2),
            "latitude": round(lat, 2),
            "longitude": round(lon, 2)
        }
    }