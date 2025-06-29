import streamlit as st
import plotly.express as px
from healthai_core.utils import load_sample_health_data, clean_text
from healthai_core.prompts import get_health_analytics_prompt
from healthai_core.model import query_model

st.set_page_config(page_title="Health Analytics", page_icon="📊")

st.title("📊 Health Analytics Dashboard")
st.markdown("Visualize and analyze your health metrics with AI-generated insights.")

# Load example health data
try:
    df = load_sample_health_data()
except Exception:
    st.error("Failed to load health data.")
    st.stop()

# Visualization
st.subheader("📈 Heart Rate Over Time")
st.plotly_chart(px.line(df, x="Date", y="HeartRate", title="Heart Rate"))

st.subheader("🩺 Blood Pressure Trends")
st.plotly_chart(px.line(df, x="Date", y=["BP_Systolic", "BP_Diastolic"], title="Blood Pressure"))

st.subheader("🍬 Blood Glucose Levels")
st.plotly_chart(px.line(df, x="Date", y="BloodGlucose", title="Blood Glucose"))

# AI Insight
st.subheader("🧠 AI Health Summary")
if st.button("Generate AI Insights"):
    metrics_summary = df.tail(7).to_string(index=False)
    prompt = get_health_analytics_prompt(metrics_summary)
    with st.spinner("Analyzing trends..."):
        ai_insight = query_model(prompt)
        st.success("AI Summary:")
        st.write(clean_text(ai_insight))
