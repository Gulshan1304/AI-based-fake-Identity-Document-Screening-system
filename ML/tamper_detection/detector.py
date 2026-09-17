from pathlib import Path
from typing import Dict, Any

from PIL import Image, ImageChops, ImageEnhance


def validate_image(image_path: str) -> bool:
    """
    Check whether the image exists and can be opened.
    """

    path = Path(image_path)

    if not path.exists():
        return False

    try:
        with Image.open(path) as image:
            image.verify()

        return True

    except Exception:
        return False


def analyze_image_quality(image_path: str) -> Dict[str, Any]:
    """
    Perform basic image-quality analysis.

    This does NOT prove that a document is tampered.
    """

    path = Path(image_path)

    try:
        with Image.open(path) as image:

            width, height = image.size

            # Very small images may be unsuitable for analysis
            low_resolution = (
                width < 500 or height < 300
            )

            return {
                "width": width,
                "height": height,
                "low_resolution": low_resolution
            }

    except Exception as error:

        return {
            "error": str(error)
        }


def analyze_metadata(image_path: str) -> Dict[str, Any]:
    """
    Inspect basic image metadata.

    Metadata alone is not evidence of tampering.
    """

    try:
        with Image.open(image_path) as image:

            metadata = image.getexif()

            return {
                "metadata_present": len(metadata) > 0,
                "metadata_count": len(metadata)
            }

    except Exception as error:

        return {
            "error": str(error)
        }


def detect_tamper_indicators(
    image_path: str
) -> Dict[str, Any]:
    """
    Main tamper-indicator analysis.

    Returns indicators that may require further review.
    """

    indicators = []

    # Step 1: Validate image
    if not validate_image(image_path):

        return {
            "status": "FAILED",
            "tamper_indicator": True,
            "reason_codes": [
                "INVALID_IMAGE"
            ],
            "message": "Image could not be processed."
        }

    # Step 2: Image quality
    quality = analyze_image_quality(image_path)

    if quality.get("low_resolution"):

        indicators.append(
            "LOW_IMAGE_RESOLUTION"
        )

    # Step 3: Metadata
    metadata = analyze_metadata(image_path)

    # Missing metadata is NOT proof of tampering
    if not metadata.get("metadata_present", False):

        indicators.append(
            "METADATA_UNAVAILABLE"
        )

    return {
        "status": "REVIEW_REQUIRED"
        if indicators
        else "NO_INDICATOR_DETECTED",

        "tamper_indicator": bool(indicators),

        "reason_codes": indicators,

        "image_quality": quality,

        "metadata": metadata,

        "message": (
            "Potential indicators require further analysis."
            if indicators
            else "No basic tamper indicators detected."
        )
    }