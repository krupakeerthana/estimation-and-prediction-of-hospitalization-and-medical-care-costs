import streamlit as st
from healthai_core.prompts import get_disease_prediction_prompt
from healthai_core.model import query_model
from healthai_core.utils import format_response

st.set_page_config(page_title="Disease Prediction", page_icon="🧪")

st.title("🧪 Disease Prediction")
st.markdown("Describe your symptoms and receive possible condition predictions.")

symptoms = st.text_area("Describe your symptoms (e.g., headache, fever, fatigue):", height=150)

if st.button("Predict Disease"):
    if symptoms.strip():
        with st.spinner("Analyzing symptoms..."):
            prompt = get_disease_prediction_prompt(symptoms)
            response = query_model(prompt)
            st.success("Potential Diagnoses:")
            st.write(format_response(response))
    else:
        st.warning("Please describe your symptoms.")
