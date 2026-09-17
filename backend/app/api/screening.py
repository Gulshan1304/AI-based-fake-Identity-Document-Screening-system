from fastapi import APIRouter, UploadFile, File
from datetime import datetime
import uuid

from app.services.anomaly_detection import detect_anomalies


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

    # ------------------------------------------------
    # Temporary document data
    # ------------------------------------------------
    #
    # Abhi OCR connect nahi hua hai.
    # Isliye uploaded document se actual fields
    # extract nahi ho rahe.
    #
    # Future:
    # Upload → OCR → document_data → anomaly detection
    #

    document_data = {
        "name": None,
        "document_number": None,
        "expiry_date": None
    }


    # ------------------------------------------------
    # Run Anomaly Detection
    # ------------------------------------------------

    anomaly_result = detect_anomalies(document_data)

    if anomaly_result["count"] > 0:
        anomaly_status = "REVIEW_REQUIRED"
    else:
        anomaly_status = "NO_ANOMALY"


    # ------------------------------------------------
    # Return Screening Result
    # ------------------------------------------------

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

            "anomaly_detection": anomaly_status
        },

        "anomaly_result": anomaly_result,

        "risk": {

            "score": None,

            "level": "NOT_AVAILABLE",

            "reason_codes": anomaly_result["anomalies"]
        },

        "created_at": datetime.utcnow().isoformat(),

        "message": (
            "Document received successfully. "
            "Anomaly detection has been executed. "
            "Further authorized human review may be required."
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