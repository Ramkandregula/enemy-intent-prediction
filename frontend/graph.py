import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Intent Threat Trend", layout="centered")

st.title("📈 Intent Threat Trend Analysis")

# Simulated time and threat score data
time_steps = np.arange(1, 21)  # Time axis
threat_score = [12, 18, 22, 30, 35, 40, 48, 55, 60, 68,
                72, 75, 78, 82, 85, 88, 90, 92, 95, 98]

# Plot threat trend
fig, ax = plt.subplots()
ax.plot(time_steps, threat_score, marker='o')

ax.set_xlabel("Time")
ax.set_ylabel("Threat Score")
ax.set_title("Enemy Intent Threat Trend Over Time")
ax.set_ylim(0, 100)

# Threshold lines
ax.axhline(30, linestyle='--', label='Low Threat')
ax.axhline(60, linestyle='--', label='Medium Threat')
ax.axhline(85, linestyle='--', label='High Threat')

ax.legend()

st.pyplot(fig)

# Threat status text
current_threat = threat_score[-1]

if current_threat < 30:
    st.success("Current Status: LOW THREAT")
elif current_threat < 60:
    st.warning("Current Status: MEDIUM THREAT")
else:
    st.error("Current Status: HIGH THREAT")