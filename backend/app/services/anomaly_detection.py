def detect_anomalies(document_data: dict):

    anomalies = []

    # Check name
    if not document_data.get("name"):
        anomalies.append("MISSING_NAME")

    # Check document number
    if not document_data.get("document_number"):
        anomalies.append("MISSING_DOCUMENT_NUMBER")

    # Check expiry date
    if not document_data.get("expiry_date"):
        anomalies.append("MISSING_EXPIRY_DATE")

    return {
        "anomalies": anomalies,
        "count": len(anomalies)
    }