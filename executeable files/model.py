import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct-v0.2")
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

def load_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
        token=HF_TOKEN
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

generator = load_pipeline()

def generate_response(prompt: str) -> str:
    output = generator(prompt, max_new_tokens=200, do_sample=True)[0]['generated_text']
    return output

