import joblib

model = joblib.load("backend/threat_model.pkl")

def predict_enemy_intent(features):
    probs = model.predict_proba([features])[0]
    idx = probs.argmax()
    confidence = round(max(probs) * 100, 2)

    label_map = {0: "LOW", 1: "MEDIUM", 2: "HIGH"}

    explanation_map = {
        0: "Low hostile indicators detected. Movement appears routine.",
        1: "Suspicious activity observed. Monitoring is advised.",
        2: "High-speed hostile movement near sensitive zone detected."
    }

    return {
        "threat_level": label_map[idx],
        "confidence": confidence,
        "explanation": explanation_map[idx]
    }