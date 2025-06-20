from huggingface_hub import InferenceClient
import os

def load_model(model_name="meta-llama/Llama-2-7b-chat-hf"):
    """Load HF Inference API client with env-based token"""
    HF_TOKEN = os.getenv("HF_TOKEN")
    if not HF_TOKEN:
        raise ValueError(
            "HF_TOKEN not found in environment variables.\n"
            "Please run:\n"
            "Windows: `set HF_TOKEN=your_api_token_here`\n"
            "Linux/Mac: `export HF_TOKEN=your_api_token_here`"
        )
    return InferenceClient(token=HF_TOKEN), None
