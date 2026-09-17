"""
Transparent rule-based risk engine.

This module produces screening indicators only.
It must not be treated as the final identity decision.
"""


def calculate_risk(indicators: dict):

    score = 0
    reason_codes = []

    if indicators.get("tampering_detected"):
        score += 30
        reason_codes.append("DOC_TAMPER_INDICATOR")

    if indicators.get("face_mismatch"):
        score += 30
        reason_codes.append("FACE_MISMATCH")

    if indicators.get("expired"):
        score += 20
        reason_codes.append("DOCUMENT_EXPIRED")

    if indicators.get("data_inconsistency"):
        score += 15
        reason_codes.append("DATA_INCONSISTENCY")

    if indicators.get("watchlist_hit"):
        score += 40
        reason_codes.append("WATCHLIST_REVIEW")

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "reason_codes": reason_codes
    }