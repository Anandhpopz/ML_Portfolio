import streamlit as st
import pickle
import spacy
import numpy as np
def run_app():
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Load the pickled Random Forest model
    with open(r"C:\Users\ACER\Desktop\ML_Portfolio\models\spacy.pkl", "rb") as file:
        model = pickle.load(file)

    # Streamlit app
    st.title("Fake News Detection")
    st.write("Enter a news title to check if it is Real or Fake:")

    # Text input
    news_title = st.text_input("News Title")

    if st.button("Predict"):
        if news_title.strip() == "":
            st.warning("Please enter a news title!")
        else:
            # Convert title to vector
            vector = nlp(news_title).vector
            vector = np.expand_dims(vector, axis=0)  # Make it 2D
            # Predict
            prediction = model.predict(vector)[0]
            result = "Real News ✅" if prediction == 1 else "Fake News ❌"
            st.success(f"Prediction: {result}")
    st.markdown("[Click here to view Proof on concept Colab notebook](https://colab.research.google.com/drive/1Yvsy5E6v6nZeCn8ZKKljohxPnf9-0uhW#scrollTo=HfF_YMD42qEK)")
    st.markdown("[Click to view details about data set](https://www.kaggle.com/datasets/algord/fake-news)")

