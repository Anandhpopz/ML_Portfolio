# apps/Salary.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

def run_app():
    # Load model
    model = joblib.load(r"models/linear_regression_model.pkl")

    # Pre-fitted LabelEncoders
    gender_encoder = LabelEncoder()
    gender_encoder.classes_ = np.array(["Female", "Male"])

    job_encoder = LabelEncoder()
    job_encoder.classes_ = np.array(["Data Analyst", "Data Scientist", "Software Engineer"])

    edu_encoder = LabelEncoder()
    edu_encoder.classes_ = np.array(["Bachelors", "Masters", "PhD"])

    st.header("Salary Prediction App")
    st.markdown("Enter your details below:")

    # Inputs
    age = st.number_input("Age", 18, 70, 25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education_level = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
    job_title = st.selectbox("Job Title", ["Data Analyst", "Data Scientist", "Software Engineer"])
    experience = st.number_input("Years of Experience", 0, 40, 2)

    # Encode categorical
    encoded_gender = gender_encoder.transform([gender])[0]
    encoded_job = job_encoder.transform([job_title])[0]
    encoded_edu = edu_encoder.transform([education_level])[0]

    # Input dataframe
    input_data = pd.DataFrame([[age, encoded_gender, encoded_edu, encoded_job, experience]],
                              columns=['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience'])

    # Predict
    if st.button("Predict Salary"):
        prediction = model.predict(input_data)
        st.success(f"Predicted Salary: ${prediction[0]:,.2f}")
