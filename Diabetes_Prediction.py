import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("model.pkl")

st.title("Diabetes Prediction System")

# Input Fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

glucose = st.number_input("Glucose", min_value=50.0, max_value=300.0, value=100.0)

blood_pressure = st.number_input("Blood Pressure", min_value=40, max_value=250, value=80)

cholesterol = st.number_input("Cholesterol", min_value=50, max_value=500, value=180)

insulin = st.number_input("Insulin", min_value=0, max_value=500, value=80)

hba1c = st.number_input("HbA1c", min_value=3.0, max_value=15.0, value=5.5)

smoking = st.selectbox("Smoking Status", ["Current", "Former", "Never"])

activity = st.selectbox("Physical Activity", ["High", "Low", "Moderate"])

family = st.selectbox("Family History", ["Yes", "No"])

# Encoding
gender = 1 if gender == "Male" else 0

smoking_dict = {
    "Current": 0,
    "Former": 1,
    "Never": 2
}
smoking = smoking_dict[smoking]

activity_dict = {
    "High": 0,
    "Low": 1,
    "Moderate": 2
}
activity = activity_dict[activity]

family = 1 if family == "Yes" else 0

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "BMI": [bmi],
        "Glucose": [glucose],
        "Blood_Pressure": [blood_pressure],
        "Cholesterol": [cholesterol],
        "Insulin": [insulin],
        "HbA1c": [hba1c],
        "Smoking_Status": [smoking],
        "Physical_Activity": [activity],
        "Family_History": [family]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Diabetes Detected")
    else:
        st.success("No Diabetes")