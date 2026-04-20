import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(page_title="Crowd Prediction Dashboard", layout="wide")

# -----------------------------
# SIDEBAR (Controls)
# -----------------------------
st.sidebar.title("⚙️ Controls")

num_people = st.sidebar.slider("Crowd Size", 10, 100, 30, key="crowd_slider")

area = st.sidebar.selectbox("Area Type", ["Mall", "Stadium", "Street", "Festival"])

model = st.sidebar.selectbox("Prediction Model", ["Basic AI", "Federated AI"])

# -----------------------------
# MAIN TITLE
# -----------------------------
st.title("📊 Crowd Behavior Prediction Dashboard")

st.markdown("🔐 Data processed locally using Federated Learning")
# Risk logic FIRST
if num_people < 30:
    risk = "Low"
elif num_people < 70:
    risk = "Medium"
else:
    risk = "High"

# THEN metrics
col1, col2, col3 = st.columns(3)

col1.metric("👥 Crowd Size", num_people)
col2.metric("⚠️ Risk Level", risk)
col3.metric("📍 Area", area)
st.subheader("🎯 Risk Indicator")

if risk == "Low":
    st.markdown("🟢 **Status: SAFE**")
elif risk == "Medium":
    st.markdown("🟡 **Status: CAUTION**")
else:
    st.markdown("🔴 **Status: DANGER**")
# -----------------------------
# LAYOUT (Columns)
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# 1. CROWD SIMULATION
# -----------------------------
with col1:
    st.subheader("👥 Crowd Simulation")

    x = [random.random() for _ in range(num_people)]
    y = [random.random() for _ in range(num_people)]

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Crowd Movement")

    st.pyplot(fig)

# -----------------------------
# 2. RISK PREDICTION
# -----------------------------
with col2:
    st.subheader("⚠️ Risk Prediction")

    if num_people < 30:
        risk = "Low"
    elif num_people < 70:
        risk = "Medium"
    else:
        risk = "High"

    if st.button("Predict Risk"):
        if risk == "Low":
            st.success("🟢 Low Risk")
        elif risk == "Medium":
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")

    # ✅ ADD HERE 👇
    st.subheader("🛠️ Mitigation Actions")

    if risk == "Low":
        st.write("Normal monitoring")
    elif risk == "Medium":
        st.write("Increase surveillance and control entry")
    else:
        st.write("Activate emergency evacuation and alert authorities")

# -----------------------------
# 3. DASHBOARD CHARTS
# -----------------------------
st.subheader("📈 Crowd Analytics")

data = {
    "Low": random.randint(10, 30),
    "Medium": random.randint(20, 50),
    "High": random.randint(10, 40)
}

df = pd.DataFrame(list(data.items()), columns=["Risk", "Count"])

st.bar_chart(df.set_index("Risk"))


st.subheader("🚨 Alerts & Actions")

if num_people < 30:
    st.info("Crowd is under control. No action required.")
elif num_people < 70:
    st.warning("Moderate crowd detected. Monitor situation.")
else:
    st.error("High crowd density! Trigger emergency response.")
