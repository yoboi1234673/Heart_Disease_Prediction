import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pickle

# Load the trained model
model = load_model("heart_disease_ann_model.h5")

# Dummy scaler – in real case, save and load the scaler used during training
# Replace this with a real scaler loaded using pickle
scaler = StandardScaler()
scaler.mean_ = np.array([54.3, 1.0, 0.7, 131.7, 246.3, 0.15, 0.52, 149.6, 0.33, 1.0, 1.6, 0.6, 2.3])  # example
scaler.scale_ = np.array([9.0, 0.5, 0.4, 17.7, 51.8, 0.36, 0.5, 22.9, 0.47, 0.6, 0.6, 0.5, 0.6])  # example

# Title
st.title("❤️ Heart Disease Prediction")

# Input fields
age = st.number_input("Age", 20, 100, 54)
sex = st.selectbox("Sex", [0, 1])  # 0: Female, 1: Male
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 130)
chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 600, 246)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]

    if prediction > 0.5:
        st.error("⚠️ High chance of heart disease.")
    else:
        st.success("✅ Low chance of heart disease.")


import pickle
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)


with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
