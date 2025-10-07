# apps/Salary.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.datasets import load_iris

def run_app():
    # Load trained Iris classification model
    model1 = joblib.load("models/iris.pkl")

    st.title("Iris Flower Classification App")
    st.markdown("Input the features of the Iris flower to predict its species.")

    # User input
    sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.0)
    sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
    petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.5)
    petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

    # Prepare input
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                              columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

    # Predict button
    if st.button("Predict"):
        pred = model1.predict(input_data)
        iris = load_iris()
        species = iris.target_names[pred[0]]  # Map numeric prediction to species name
        st.success(f"Predicted Iris species: **{species}**")
