from fastapi import APIRouter, HTTPException
from app.schemas.common import Email
from app.schemas.lead import LeadScoreResponse
from app.services.lead import calculate_lead_score

router = APIRouter(prefix="/lead", tags=["lead"])


@router.post("/score", response_model=LeadScoreResponse)
async def score_lead(payload: Email):
    try:
        result = calculate_lead_score(payload.subject, payload.body)
        print(result)
        return LeadScoreResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lead scoring failed: {str(e)}")