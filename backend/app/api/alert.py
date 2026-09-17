from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"]
)


alerts = []


class AlertCreate(BaseModel):
    alert_type: str
    message: str
    severity: str = "MEDIUM"


@router.get("/")
def get_alerts():
    return alerts


@router.post("/")
def create_alert(alert: AlertCreate):

    new_alert = {
        "alert_id": str(uuid4()),
        "alert_type": alert.alert_type,
        "message": alert.message,
        "severity": alert.severity,
        "status": "OPEN",
        "created_at": datetime.utcnow().isoformat()
    }

    alerts.append(new_alert)

    return new_alert


@router.patch("/{alert_id}/resolve")
def resolve_alert(alert_id: str):

    for alert in alerts:

        if alert["alert_id"] == alert_id:

            alert["status"] = "RESOLVED"

            return alert

    return {
        "message": "Alert not found"
    }