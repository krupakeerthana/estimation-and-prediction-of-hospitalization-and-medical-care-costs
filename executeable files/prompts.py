# healthai_core/prompts.py

def disease_prompt(symptoms: str) -> str:
    return f"Given the symptoms: {symptoms}, what possible diseases could the patient have?"

def treatment_prompt(condition: str) -> str:
    return f"Suggest a treatment plan for: {condition}"

def patient_query_prompt(query: str) -> str:
    return f"Medical question: {query}"
