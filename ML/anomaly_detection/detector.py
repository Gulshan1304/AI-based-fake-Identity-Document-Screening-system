from typing import Dict, List, Any


REQUIRED_FIELDS = [
    "name",
    "document_number",
    "expiry_date"
]


def detect_anomalies(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Basic rule-based anomaly detection.

    This is a prototype and does not determine
    whether a document is genuine or fraudulent.
    """

    anomalies: List[str] = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        value = data.get(field)

        if value is None or str(value).strip() == "":
            anomalies.append(f"MISSING_{field.upper()}")

    # Check name
    name = data.get("name")

    if name and len(str(name).strip()) < 2:
        anomalies.append("INVALID_NAME_FORMAT")

    # Check document number
    document_number = data.get("document_number")

    if document_number and len(str(document_number).strip()) < 4:
        anomalies.append("SHORT_DOCUMENT_NUMBER")

    # Check expiry date
    if data.get("expiry_date") is None:
        anomalies.append("EXPIRY_DATE_UNAVAILABLE")

    return {
        "anomaly_detected": len(anomalies) > 0,
        "count": len(anomalies),
        "reason_codes": anomalies
    }