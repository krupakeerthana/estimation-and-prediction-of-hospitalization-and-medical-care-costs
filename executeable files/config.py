import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_config():
    config = {
        "HF_TOKEN": os.getenv("HF_TOKEN"),
        "MODEL_NAME": os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct-v0.1")
    }
    if not config["HF_TOKEN"]:
        raise ValueError("HF_TOKEN is not set in the environment.")
    return config
