import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import os

# Set your model from Hugging Face
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if HUGGINGFACE_TOKEN is None:
    st.error("Missing HUGGINGFACE_TOKEN environment variable.")
    st.stop()

@st.cache_resource
def load_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HUGGINGFACE_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
        token=HUGGINGFACE_TOKEN
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

generator = load_pipeline()

def generate_response(prompt):
    output = generator(prompt, max_new_tokens=200, do_sample=True)[0]['generated_text']
    return output

# Streamlit App Configuration
st.set_page_config(page_title="HealthAI", layout="wide")
st.title("🧠 HealthAI: Intelligent Healthcare Assistant")

# Sidebar Navigation
section = st.sidebar.selectbox("Choose Feature", ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"])

# Patient Chat
if section == "Patient Chat":
    st.header("🗣️ Patient Chat")
    query = st.text_input("Ask a medical question:")
    if st.button("Submit") and query:
        with st.spinner("Getting response..."):
            response = generate_response(f"Medical question: {query}")
            st.success(response)

# Disease Prediction (Mocked)
elif section == "Disease Prediction":
    st.header("🔍 Disease Prediction")
    symptoms = st.text_area("Describe your symptoms (e.g., headache, fever, fatigue):")
    if st.button("Predict"):
        prompt = f"Given the symptoms: {symptoms}, what possible diseases could the patient have?"
        response = generate_response(prompt)
        st.info(response)
        st.warning("Note: This is not a substitute for professional medical advice.")

# Treatment Plans (Mocked)
elif section == "Treatment Plans":
    st.header("💊 Treatment Plans")
    condition = st.text_input("Enter diagnosed condition:")
    if st.button("Get Treatment Plan"):
        prompt = f"Suggest a treatment plan for: {condition}"
        response = generate_response(prompt)
        st.info(response)
        st.warning("Always consult a doctor before starting any treatment.")

# Health Analytics
elif section == "Health Analytics":
    st.header("📊 Health Analytics Dashboard")

    data = pd.DataFrame({
        "Date": pd.date_range(start="2025-06-01", periods=10),
        "Heart Rate": [72, 74, 75, 76, 74, 73, 77, 79, 76, 75],
        "Blood Pressure": [120, 122, 121, 119, 118, 121, 123, 124, 125, 123],
        "Glucose": [95, 96, 98, 97, 99, 100, 98, 97, 96, 95]
    })

    st.subheader("📈 Heart Rate")
    st.plotly_chart(px.line(data, x="Date", y="Heart Rate", title="Heart Rate Trend"))

    st.subheader("🩸 Blood Pressure")
    st.plotly_chart(px.line(data, x="Date", y="Blood Pressure", title="Blood Pressure Trend"))

    st.subheader("🍬 Glucose Levels")
    st.plotly_chart(px.line(data, x="Date", y="Glucose", title="Glucose Trend"))

    st.subheader("📌 Summary")
    st.dataframe(data.set_index("Date"))
