from scaledown_api import compress_code
from llm_client import review_with_llm
def run_review(code: str) -> str:
    compressed = compress_code(code)
    return review_with_llm(compressed)
