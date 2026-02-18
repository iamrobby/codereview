import os
import json
from typing import Any
from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing in .env")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"



def _extract_text(resp: Any) -> str:
  if resp is None:
    return ""
  if isinstance(resp, str):
    return resp
  if isinstance(resp, dict):
    # Common keys
    for key in ("text", "output_text", "content", "response"):
      v = resp.get(key)
      if isinstance(v, str):
        return v
      if isinstance(v, list) and v:
        if all(isinstance(i, str) for i in v):
          return "\n".join(v)
        return _extract_text(v[0])
    if "candidates" in resp and resp["candidates"]:
      return _extract_text(resp["candidates"][0])
    if "choices" in resp and resp["choices"]:
      return _extract_text(resp["choices"][0])
    return json.dumps(resp)

  # Objects with attributes
  for attr in ("text", "output_text", "content", "response", "message", "choices", "candidates"):
    if hasattr(resp, attr):
      val = getattr(resp, attr)
      if isinstance(val, str):
        return val
      if isinstance(val, list) and val:
        return _extract_text(val[0])
      return _extract_text(val)

  return str(resp)


def review_with_llm(compressed_code: str) -> str:
    if not compressed_code or not compressed_code.strip():
        return "No code provided for review."

    prompt = f"""
You are a senior software engineer performing a strict code review.

Analyze the following COMPRESSED source code.
Identify issues in:
1. Bugs and logical errors
2. Security vulnerabilities
3. Performance problems
4. Code style and maintainability

Respond ONLY in valid JSON with this schema:

{{
  "issues": [
    {{
      "issue_type": "string",
      "severity": "low | medium | high",
      "line_number": number,
      "explanation": "string",
      "suggested_fix": "string"
    }}
  ]
}}

CODE:
{compressed_code}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.2,
                "response_mime_type": "application/json",
            },
        )

        text = _extract_text(response)
        return json.loads(text)

    except json.JSONDecodeError:
        raise RuntimeError(f"Gemini returned invalid JSON:\n{text[:500]}")

    except Exception as exc:
        raise RuntimeError(f"Gemini request failed: {exc}") from exc

