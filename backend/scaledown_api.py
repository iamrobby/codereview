import requests

SCALEDOWN_API_URL = "https://api.scaledown.xyz/compress/raw/"
SCALEDOWN_API_KEY = "HrQT4walIl4AT3XFpM0Ed96P8pZ00vrzaO8dX2u0"

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
    print("ScaleDown raw response:", response.json())

    response.raise_for_status()
    data = response.json()
    
    # Extract the compressed code from the response
    if isinstance(data, dict):
        # Try common response keys
        for key in ("output", "result", "text", "compressed", "code", "content"):
            if key in data and isinstance(data[key], str):
                return data[key]
        # If none found, return the JSON string representation
        return str(data)
    
    return str(data) 
