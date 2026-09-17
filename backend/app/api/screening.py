from fastapi import APIRouter, UploadFile, File
from datetime import datetime
import uuid

router = APIRouter(
    prefix="/api/screening",
    tags=["Screening"]
)


@router.post("/")
async def screen_document(document: UploadFile = File(...)):
    """
    Upload a document and start AI-assisted screening.
    """

    screening_id = f"SCR-{uuid.uuid4().hex[:8].upper()}"

    return {
        "screening_id": screening_id,
        "filename": document.filename,
        "content_type": document.content_type,
        "status": "REVIEW_REQUIRED",

        "checks": {
            "document_authentication": "PENDING",
            "tamper_detection": "PENDING",
            "face_verification": "PENDING",
            "expiry_validation": "PENDING",
            "watchlist_screening": "PENDING",
            "anomaly_detection": "PENDING"
        },

        "risk": {
            "score": None,
            "level": "NOT_AVAILABLE",
            "reason_codes": []
        },

        "created_at": datetime.utcnow().isoformat(),

        "message": (
            "Document received successfully. "
            "AI-assisted screening requires further processing "
            "and authorized human review."
        )
    }


@router.get("/{screening_id}")
async def get_screening(screening_id: str):
    """
    Get screening result using screening ID.
    """

    return {
        "screening_id": screening_id,
        "status": "REVIEW_REQUIRED",
        "message": "Screening result retrieved successfully."
    }