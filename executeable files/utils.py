# healthai_core/utils.py

import pandas as pd

def load_health_data():
    return pd.read_csv("data/sample_metrics.csv", parse_dates=["Date"])
def clean_text(text: str) -> str:
    return ' '.join(text.split())

def format_response(text: str) -> str:
    return text.strip().replace('\n\n', '\n')
    
