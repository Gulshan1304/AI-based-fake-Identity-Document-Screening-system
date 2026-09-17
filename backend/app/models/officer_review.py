from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class OfficerReviewCreate(BaseModel):
    screening_id: str

    decision: str = Field(
        ...,
        description="Officer review decision"
    )

    remarks: Optional[str] = None


class OfficerReview(BaseModel):
    review_id: str

    screening_id: str

    officer_id: str

    decision: str

    remarks: Optional[str] = None

    reviewed_at: datetime

    class Config:
        from_attributes = True