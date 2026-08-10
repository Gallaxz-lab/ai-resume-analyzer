from pydantic import BaseModel
from typing import List

class ResumeAnalysisResponse(BaseModel):
    score: int
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]