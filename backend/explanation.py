"""
explanation.py
---------------
Rule-based AI explanation engine.
Deterministic, explainable, no randomness.
"""

def explanation_engine(speed, distance, direction, hospitality):
    """
    Generate a human-readable explanation
    based on satellite behavior indicators.
    """

    # 🔴 HIGH THREAT
    if speed > 25 and distance < 20:
        return (
            "High-speed movement detected in close proximity to a sensitive zone, "
            "indicating potential hostile intent."
        )

    if speed > 60 and distance < 40 and hospitality < 0.3:
        return (
            "Moderate to high speed combined with low hospitality index "
            "suggests suspicious or adversarial behavior."
        )

    # 🟠 MEDIUM THREAT
    if direction in range(90, 150) and distance < 50:
        return (
            "Movement direction aligns with a known strategic corridor; "
            "continuous monitoring is advised."
        )

    if speed > 50 and distance < 60:
        return (
            "Elevated movement activity observed at moderate distance, "
            "indicating possible reconnaissance behavior."
        )

    # 🟢 LOW THREAT
    if speed < 40 and distance > 60:
        return (
            "Low-speed activity detected at a safe distance, "
            "indicating routine or non-hostile movement."
        )

    if hospitality > 0.7:
        return (
            "High hospitality index suggests cooperative or non-adversarial behavior."
        )

    # ⚪ DEFAULT
    return (
        "No critical hostile indicators detected at this time. "
        "Situation remains stable."
    )