from transformers import pipeline
from .config import load_config

# Load config
config = load_config()

# Set up text generation pipeline using Hugging Face model
text_generator = pipeline(
    "text-generation",
    model=config["MODEL_NAME"],
    token=config["HF_TOKEN"]
)

def query_model(prompt: str, max_tokens: int = 512):
    """Query the LLM with a prompt and return the generated response."""
    response = text_generator(prompt, max_length=max_tokens, do_sample=True, temperature=0.7)
    return response[0]["generated_text"].strip()
