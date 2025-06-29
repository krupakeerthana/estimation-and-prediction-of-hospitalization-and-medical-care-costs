# healthai_core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

def get_hf_token():
    token = os.getenv("HUGGINGFACE_TOKEN")
    if not token:
        raise ValueError("Missing Hugging Face token. Set HUGGINGFACE_TOKEN in your .env file.")
    return token
