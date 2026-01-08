import joblib
from explanation_engine import generate_explanation

model = joblib.load("trained_model.pkl")
importance = joblib.load("feature_importance.pkl")

def predict_enemy_intent(features):
    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0]) * 100

    top_features = sorted(importance, key=importance.get, reverse=True)[:3]

    explanation_map = {
        "ATTACK": "Rapid movement and high hostility near border",
        "SURVEILLANCE": "Moderate activity detected, monitoring advised",
        "NO_THREAT": "Low hostile indicators observed"
    }

    return {
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "explanation": explanation_map[prediction],
        "top_features": top_features,
        "next_action": "Deploy forces" if prediction == "ATTACK" else "Monitor"
    }