from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ScreeningChecks(BaseModel):
    document_authentication: str = "PENDING"
    tamper_detection: str = "PENDING"
    face_verification: str = "PENDING"
    expiry_validation: str = "PENDING"
    watchlist_screening: str = "PENDING"
    anomaly_detection: str = "PENDING"


class RiskAssessment(BaseModel):
    score: Optional[int] = Field(
        default=None,
        ge=0,
        le=100
    )

    level: str = "NOT_AVAILABLE"

    reason_codes: List[str] = []


class ScreeningCreate(BaseModel):
    document_id: Optional[str] = None


class ScreeningResult(BaseModel):
    screening_id: str

    document_id: Optional[str] = None

    status: str = "PENDING"

    checks: ScreeningChecks

    risk: RiskAssessment

    message: Optional[str] = None

    created_at: datetime