import streamlit as st
import requests
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
st.title("🚨 AI Threat Detection Dashboard")

if st.button("🔍 Predict Threat"):
    res = requests.get("http://127.0.0.1:8000/detect-threat").json()

    threat = res["threat_level"]
    confidence = res["confidence"]
    explanation = res["explanation"]
    data = res["inputs"]

    if threat == "HIGH":
        st.error(f"🚨 HIGH THREAT ({confidence}%)")
    elif threat == "MEDIUM":
        st.warning(f"⚠️ MEDIUM THREAT ({confidence}%)")
    else:
        st.success(f"✅ LOW THREAT ({confidence}%)")

    st.info(explanation)

    df = pd.DataFrame({
        "Parameter": ["Speed", "Distance", "Hospitality"],
        "Value": [data["speed"], data["distance"], data["hospitality"] * 100]
    })

    st.altair_chart(
        alt.Chart(df).mark_bar().encode(
            x="Parameter",
            y="Value",
            color="Parameter"
        ),
        use_container_width=True
    )
