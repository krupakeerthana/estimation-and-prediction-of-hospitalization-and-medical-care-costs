# healthai_core/utils.py

def clean_text(text: str) -> str:
    return ' '.join(text.split())

def format_response(text: str) -> str:
    return text.strip().replace('\n\n', '\n')
