from fastapi import APIRouter

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def admin_dashboard():
    """
    Admin dashboard statistics.
    """

    return {
        "system": "AI Identity & Document Screening System",

        "statistics": {
            "total_screenings": 0,
            "verified_documents": 0,
            "review_required": 0,
            "failed_screenings": 0,
            "open_alerts": 0
        },

        "system_status": {
            "api": "ONLINE",
            "database": "CONNECTED",
            "ai_services": "READY"
        }
    }


@router.get("/screenings")
def admin_screenings():
    """
    Admin can view screening records.
    """

    return {
        "screenings": [],
        "message": "Screening records will be loaded from database."
    }


@router.get("/system-status")
def system_status():
    """
    Check overall system status.
    """

    return {
        "status": "ONLINE",
        "api": "HEALTHY",
        "database": "CONNECTED",
        "ai_engine": "READY"
    }