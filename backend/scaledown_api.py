import os
from dotenv import load_dotenv
import requests

load_dotenv()

SCALEDOWN_API_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")

if not SCALEDOWN_API_KEY:
    raise RuntimeError(
        "SCALEDOWN_API_KEY environment variable is not set. "
        "Set it in a .env file or in the environment before running the app."
    )


def compress_code(code: str) -> str:
    payload = {
        "context": "You are compressing source code while preserving logic and structure.",
        "prompt": code,
        "model": "gpt-4o"
    }

    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        SCALEDOWN_API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )
    print("ScaleDown status:", response.status_code)
    try:
        raw = response.json()
    except ValueError:
        raw = response.text
    print("ScaleDown raw response:", raw)

    response.raise_for_status()
    data = raw
    
    # Extract the compressed code from the response
    if isinstance(data, dict):
        # Try common response keys
        for key in ("output", "result", "text", "compressed", "code", "content"):
            if key in data and isinstance(data[key], str):
                return data[key]
        # If none found, return the JSON string representation
        return str(data)

    return str(data)
