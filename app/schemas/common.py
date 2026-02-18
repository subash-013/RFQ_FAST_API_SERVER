from pydantic import BaseModel, Field


class Email(BaseModel):
    """Shared email schema"""
    subject: str | None = None
    body: str = Field(min_length=10, description="Email body content")