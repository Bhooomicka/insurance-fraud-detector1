import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/insurance_fraud_model.pkl')

st.set_page_config(page_title="Insurance Fraud Detector", layout="centered")
st.title("🕵️ Insurance Fraud Detector")
st.write("Enter claim details below to predict if it's fraudulent.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, step=1)
policy_state = st.selectbox("Policy State", ["IN", "OH", "IL"])
incident_type = st.selectbox("Incident Type", ["Single Vehicle Collision", "Multi-vehicle Collision", "Parked Car", "Vehicle Theft"])
incident_severity = st.selectbox("Incident Severity", ["Minor Damage", "Major Damage", "Total Loss"])
total_claim_amount = st.number_input("Total Claim Amount", min_value=0, step=100)

# Convert to dataframe for prediction
input_dict = {
    'age': age,
    'total_claim_amount': total_claim_amount,
    'policy_state_OH': int(policy_state == 'OH'),
    'policy_state_IN': int(policy_state == 'IN'),
    'incident_type_Parked Car': int(incident_type == 'Parked Car'),
    'incident_type_Single Vehicle Collision': int(incident_type == 'Single Vehicle Collision'),
    'incident_type_Vehicle Theft': int(incident_type == 'Vehicle Theft'),
    'incident_severity_Major Damage': int(incident_severity == 'Major Damage'),
    'incident_severity_Minor Damage': int(incident_severity == 'Minor Damage'),
}

df_input = pd.DataFrame([input_dict])

# Predict
if st.button("🚨 Predict Fraud"):
    prediction = model.predict(df_input)[0]
    probability = model.predict_proba(df_input)[0][prediction]

    if prediction == 1:
        st.error(f"Fraudulent Claim Detected! Confidence: {probability:.2f}")
    else:
        st.success(f"Legitimate Claim. Confidence: {probability:.2f}")
