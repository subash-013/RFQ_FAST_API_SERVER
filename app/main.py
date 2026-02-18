from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router
from contextlib import asynccontextmanager
from app.api.dependencies import fetch_and_configure_lm
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup – runs once when server starts
    print("🚀 Starting RFQ Lead API...")
    fetch_and_configure_lm()          # ← your initialization happens here
    print("✅ LLM / DSPy configured")
    yield
    # Shutdown – runs when server stops
    print("🛑 Shutting down RFQ Lead API...")

app = FastAPI(
    title="RFQ Lead API",
    description="Classify emails as RFQ and score lead quality",
    version="0.1.0",
    lifespan = lifespan,
    docs_url="/docs" if settings.env == "development" else None,
)

app.include_router(api_router)


@app.get("/", include_in_schema=False)   # optional: hide root from docs
@app.get("/health", tags=["system"])
async def health_check():
    return {"status": "healthy", "env": settings.env}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.port ,reload=True,log_level="debug")