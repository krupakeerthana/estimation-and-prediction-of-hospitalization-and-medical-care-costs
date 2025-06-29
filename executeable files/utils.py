import re
import pandas as pd

def clean_text(text: str) -> str:
    """Basic cleanup for generated text output."""
    return re.sub(r"\s+", " ", text).strip()

def format_response(response: str, max_length: int = 1000) -> str:
    """Shorten and clean long AI outputs for UI display."""
    if len(response) > max_length:
        response = response[:max_length] + "..."
    return clean_text(response)

def load_sample_health_data(filepath: str = "data/sample_metrics.csv") -> pd.DataFrame:
    """Load health metric data for analytics."""
    return pd.read_csv(filepath)
