from pydantic import BaseModel, Field


class LeadScoreResponse(BaseModel):
    score: int = Field(..., ge=0, le=100)
    label: str = Field(..., pattern="^(Hot|Warm|Cold)$")
    explanation: str