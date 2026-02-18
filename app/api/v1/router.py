from fastapi import APIRouter

from .endpoints.rfq import router as rfq_router
from .endpoints.lead import router as lead_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(rfq_router)
api_router.include_router(lead_router)