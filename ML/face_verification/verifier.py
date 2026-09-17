from typing import Dict, Any


def verify_face(
    reference_image: str,
    document_image: str
) -> Dict[str, Any]:
    """
    Prototype face verification interface.

    Actual biometric model should be integrated here
    only with appropriately authorized data and testing.
    """

    if not reference_image:
        return {
            "status": "NOT_AVAILABLE",
            "match": None,
            "similarity": None,
            "message": "Reference image not provided."
        }

    if not document_image:
        return {
            "status": "NOT_AVAILABLE",
            "match": None,
            "similarity": None,
            "message": "Document image not provided."
        }

    # Placeholder result.
    # Replace this with a validated verification model later.
    return {
        "status": "PENDING",
        "match": None,
        "similarity": None,
        "message": (
            "Face verification model is not connected yet."
        )
    }