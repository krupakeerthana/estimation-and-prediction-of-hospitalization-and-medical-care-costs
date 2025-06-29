def get_patient_chat_prompt(question: str) -> str:
    return f"""
You are an empathetic AI healthcare assistant. A user has asked a health question.
Respond with verified, easy-to-understand advice and indicate if they should consult a doctor.
Question: {question}
"""

def get_disease_prediction_prompt(symptoms: str) -> str:
    return f"""
You are a medical assistant AI. Based on the following symptoms, suggest possible diagnoses with probabilities.
Also recommend the next steps.
Symptoms: {symptoms}
"""

def get_treatment_plan_prompt(condition: str) -> str:
    return f"""
You are a digital doctor assistant. Given the condition '{condition}', provide a concise treatment plan:
- Medication
- Lifestyle recommendations
- Follow-up tests (if any)
"""

def get_health_analytics_prompt(metrics_summary: str) -> str:
    return f"""
You are an AI health analyst. Based on these metrics: {metrics_summary}, provide insights and improvement suggestions.
Focus on trends and abnormalities.
"""
