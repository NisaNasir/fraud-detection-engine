import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb

# 1. Page Configuration
st.set_page_config(
    page_title="Fintech Transaction Monitoring & Fraud Engine",
    layout="wide"
)

st.title("🛡️ Real-Time Transaction Monitoring & Fraud Detection Engine")
st.markdown(
    "Automated fraud risk scoring and transaction auditing system for digital banks & payment gateways."
)

st.sidebar.header("Risk Operations Control")
risk_threshold = st.sidebar.slider(
    "Decision Risk Threshold", 
    min_value=0.05, 
    max_value=0.95, 
    value=0.30, 
    step=0.05,
    help="Transactions with fraud probability above this threshold trigger automatic block or manual review."
)

st.sidebar.subheader("Simulate Transaction Attributes")
scaled_amount = st.sidebar.slider("Scaled Amount Index", -1.0, 10.0, 1.5)
v14_val = st.sidebar.slider("V14 Indicator (Anomaly Factor)", -15.0, 5.0, -4.2)
v17_val = st.sidebar.slider("V17 Indicator (Anomaly Factor)", -15.0, 5.0, -3.8)
v4_val = st.sidebar.slider("V4 Indicator (Behavioral Flag)", -5.0, 10.0, 2.5)

# Calculate mock fraud probability score based on key SHAP feature impact
risk_score_raw = (v4_val * 0.35) - (v14_val * 0.45) - (v17_val * 0.40) + (scaled_amount * 0.20)
fraud_probability = float(1 / (1 + np.exp(-risk_score_raw + 1.5)))

# Display Risk Evaluation
if st.button("Evaluate Transaction Risk"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Fraud Probability Score", f"{fraud_probability:.2%}")
    with col2:
        st.metric("Configured Threshold", f"{risk_threshold:.2%}")
    with col3:
        if fraud_probability >= risk_threshold:
            st.error("ACTION REQUIRED: REJECT / BLOCK TRANSACTION")
        elif fraud_probability >= (risk_threshold * 0.7):
            st.warning("ACTION REQUIRED: TRIGGER 2FA / OTP STEP-UP")
        else:
            st.success("STATUS: APPROVED")
            
    st.markdown("---")
    st.subheader("Automated Audit & Flagging Drivers")
    
    flag_triggered = False
    if v14_val < -3.0:
        st.write("⚠️ **Critical Anomaly in V14:** Negative deviation exceeds safe pattern thresholds.")
        flag_triggered = True
    if v17_val < -3.0:
        st.write("⚠️ **High Risk Profile (V17):** Unusually high variance detected in card activity profile.")
        flag_triggered = True
    if scaled_amount > 3.0:
        st.write("ℹ️ **High Value Transaction:** Transfer amount is significantly above standard velocity baseline.")
        flag_triggered = True
        
    if not flag_triggered:
        st.write("✅ **Standard Pattern:** Transaction metrics reflect nominal user spending behaviors.")
