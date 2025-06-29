import streamlit as st
from healthai_core.prompts import get_treatment_plan_prompt
from healthai_core.model import query_model
from healthai_core.utils import format_response

st.set_page_config(page_title="Treatment Plans", page_icon="💊")

st.title("💊 Treatment Plan Generator")
st.markdown("Enter a diagnosed condition to get a suggested treatment plan.")

condition = st.text_input("Enter your medical condition (e.g., hypertension):")

if st.button("Generate Treatment Plan"):
    if condition.strip():
        with st.spinner("Creating treatment plan..."):
            prompt = get_treatment_plan_prompt(condition)
            response = query_model(prompt)
            st.success("Suggested Treatment Plan:")
            st.write(format_response(response))
    else:
        st.warning("Please enter a condition.")
