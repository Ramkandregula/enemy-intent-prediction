import streamlit as st 
import requests 
if st.button("🚨 THREAT DETECTION", use_container_width=True):
    try:
        res = requests.post("http://127.0.0.1:8000/detect-threat", timeout=5)

        if res.status_code != 200:
            st.error("Backend error")
            st.stop()

        data = res.json()

        # ✅ HANDLE BACKEND ERROR RESPONSE
        if "error" in data:
            st.error(data["error"])
            st.stop()

        # ✅ SAFE ACCESS
        st.success(f"Threat Level: {data['threat_level']}")
        st.info(f"AI Explanation: {data['explanation']}")

        with st.expander("📡 Satellite data used"):
            st.json(data["used_data"])

    except Exception as e:
        st.error(f"Backend connection failed: {e}")