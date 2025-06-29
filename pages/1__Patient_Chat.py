import streamlit as st
from healthai_core.prompts import get_patient_chat_prompt
from healthai_core.model import query_model
from healthai_core.utils import format_response

st.set_page_config(page_title="Patient Chat", page_icon="💬")

st.title("💬 Patient Chat")
st.markdown("Ask any health-related question and get helpful, AI-generated guidance.")

user_input = st.text_area("Enter your question:", height=120)

if st.button("Ask AI"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            prompt = get_patient_chat_prompt(user_input)
            response = query_model(prompt)
            st.success("Here's the AI's response:")
            st.write(format_response(response))
    else:
        st.warning("Please enter a question.")
