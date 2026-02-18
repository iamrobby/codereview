from fastapi import FastAPI
from models import  ReviewResponse
from review_engine import run_review
from pydantic import BaseModel

app = FastAPI()

class ReviewRequest(BaseModel):
    code: str


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/review", response_model=ReviewResponse)
def review_code(req: ReviewRequest):
    result = run_review(req.code)
    return result
