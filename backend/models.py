from pydantic import BaseModel
from typing import List

class ReviewRequest(BaseModel):
    code: str
    language: str

class Issue(BaseModel):
    issue_type: str
    severity: str
    line_number: int
    explanation: str
    suggested_fix: str

class ReviewResponse(BaseModel):
    issues: List[Issue]
