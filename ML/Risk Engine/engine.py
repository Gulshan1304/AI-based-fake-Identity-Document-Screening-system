from typing import Dict, Any, List


# ---------------------------------------------------------
# RISK WEIGHTS
# ---------------------------------------------------------

RISK_WEIGHTS = {
    "tamper_detection": 30,
    "license_validation": 25,
    "anomaly_detection": 20,
    "face_verification": 15,
    "ocr": 10
}


# ---------------------------------------------------------
# LEVEL CALCULATION
# ---------------------------------------------------------

def get_risk_level(score: int) -> str:
    """
    Convert risk score into a risk level.
    """

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"


# ---------------------------------------------------------
# TAMper RESULT
# ---------------------------------------------------------

def evaluate_tamper(result: Dict[str, Any]) -> tuple:
    """
    Evaluate tamper detection result.
    """

    score = 0
    reasons: List[str] = []

    if result.get("tamper_indicator") is True:

        score = RISK_WEIGHTS["tamper_detection"]

        reasons.extend(
            result.get("reason_codes", [])
        )

    return score, reasons


# ---------------------------------------------------------
# LICENSE VALIDATION RESULT
# ---------------------------------------------------------

def evaluate_license(result: Dict[str, Any]) -> tuple:
    """
    Evaluate license/document validation result.
    """

    score = 0
    reasons: List[str] = []

    status = result.get("status")

    if status == "FAILED":

        score = RISK_WEIGHTS["license_validation"]

    elif status == "REVIEW_REQUIRED":

        score = 15

    reasons.extend(
        result.get("reason_codes", [])
    )

    return score, reasons


# ---------------------------------------------------------
# ANOMALY RESULT
# ---------------------------------------------------------

def evaluate_anomaly(result: Dict[str, Any]) -> tuple:
    """
    Evaluate anomaly detection result.
    """

    score = 0
    reasons: List[str] = []

    if result.get("anomaly_detected") is True:

        count = result.get("count", 1)

        # Maximum contribution = 20
        score = min(
            count * 5,
            RISK_WEIGHTS["anomaly_detection"]
        )

        reasons.extend(
            result.get("reason_codes", [])
        )

    return score, reasons


# ---------------------------------------------------------
# FACE VERIFICATION RESULT
# ---------------------------------------------------------

def evaluate_face(result: Dict[str, Any]) -> tuple:
    """
    Evaluate face verification result.
    """

    score = 0
    reasons: List[str] = []

    status = result.get("status")

    if status == "FAILED":

        score = RISK_WEIGHTS["face_verification"]

        reasons.append(
            "FACE_VERIFICATION_FAILED"
        )

    elif status == "MISMATCH":

        score = RISK_WEIGHTS["face_verification"]

        reasons.append(
            "FACE_MISMATCH"
        )

    elif status == "NOT_AVAILABLE":

        reasons.append(
            "FACE_VERIFICATION_UNAVAILABLE"
        )

    return score, reasons


# ---------------------------------------------------------
# OCR RESULT
# ---------------------------------------------------------

def evaluate_ocr(result: Dict[str, Any]) -> tuple:
    """
    Evaluate OCR result.
    """

    score = 0
    reasons: List[str] = []

    if not result.get("success", False):

        score = RISK_WEIGHTS["ocr"]

        reasons.append(
            "OCR_FAILED"
        )

    else:

        fields = result.get("fields", {})

        required_fields = [
            "name",
            "document_number",
            "expiry_date"
        ]

        for field in required_fields:

            if not fields.get(field):

                reasons.append(
                    f"MISSING_{field.upper()}"
                )

        if reasons:

            score = min(
                len(reasons) * 3,
                RISK_WEIGHTS["ocr"]
            )

    return score, reasons


# ---------------------------------------------------------
# MAIN RISK ENGINE
# ---------------------------------------------------------

def calculate_risk(
    ocr_result: Dict[str, Any],
    tamper_result: Dict[str, Any],
    license_result: Dict[str, Any],
    anomaly_result: Dict[str, Any],
    face_result: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Combine all screening results and calculate
    an AI-assisted risk score.

    This score is NOT a final fraud decision.
    """

    total_score = 0
    reason_codes: List[str] = []

    # OCR
    score, reasons = evaluate_ocr(
        ocr_result
    )

    total_score += score
    reason_codes.extend(reasons)

    # Tamper Detection
    score, reasons = evaluate_tamper(
        tamper_result
    )

    total_score += score
    reason_codes.extend(reasons)

    # License Validation
    score, reasons = evaluate_license(
        license_result
    )

    total_score += score
    reason_codes.extend(reasons)

    # Anomaly Detection
    score, reasons = evaluate_anomaly(
        anomaly_result
    )

    total_score += score
    reason_codes.extend(reasons)

    # Face Verification
    score, reasons = evaluate_face(
        face_result
    )

    total_score += score
    reason_codes.extend(reasons)

    # Make sure score stays between 0 and 100
    total_score = min(
        total_score,
        100
    )

    # Remove duplicate reason codes
    reason_codes = list(
        dict.fromkeys(reason_codes)
    )

    # Calculate level
    risk_level = get_risk_level(
        total_score
    )

    # Determine screening status
    if total_score >= 40:

        status = "REVIEW_REQUIRED"

    else:

        status = "SCREENING_OK"

    return {
        "score": total_score,
        "level": risk_level,
        "status": status,
        "reason_codes": reason_codes,
        "message": (
            "AI screening indicates that further "
            "review may be required."
            if status == "REVIEW_REQUIRED"
            else
            "No major risk indicators were detected "
            "by the current screening rules."
        )
    }