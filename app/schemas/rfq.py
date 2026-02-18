from pydantic import BaseModel, Field


class RFQClassificationResponse(BaseModel):
    is_rfq: bool
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str