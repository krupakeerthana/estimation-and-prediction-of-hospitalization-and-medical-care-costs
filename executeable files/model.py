# healthai_core/model.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from healthai_core.config import get_hf_token

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

def load_pipeline():
    token = get_hf_token()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=token)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
        token=token
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

generator = load_pipeline()

def generate_response(prompt: str) -> str:
    output = generator(prompt, max_new_tokens=200, do_sample=True)[0]['generated_text']
    return output
