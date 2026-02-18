from fastapi import APIRouter, HTTPException
from app.schemas.common import Email
from app.schemas.rfq import RFQClassificationResponse
from app.services.rfq import classify_is_rfq

router = APIRouter(prefix="/rfq", tags=["rfq"])


@router.post("/classify", response_model=RFQClassificationResponse)
async def classify_rfq(payload: Email):
    try:
        result = classify_is_rfq(payload.subject, payload.body)
        return RFQClassificationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RFQ classification failed: {str(e)}")