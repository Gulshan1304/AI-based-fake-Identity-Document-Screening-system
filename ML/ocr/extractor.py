from pathlib import Path
from typing import Dict, Any

from PIL import Image
import pytesseract


def extract_text(image_path: str) -> str:
    """
    Extract text from an image using OCR.
    """

    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    image = Image.open(path)

    text = pytesseract.image_to_string(image)

    return text


def extract_document_fields(text: str) -> Dict[str, Any]:
    """
    Basic field extraction from OCR text.

    This is only a prototype.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    result = {
        "name": None,
        "document_number": None,
        "expiry_date": None,
        "raw_text": text,
        "lines_detected": len(lines)
    }

    # Very simple prototype extraction
    for line in lines:

        lower_line = line.lower()

        if lower_line.startswith("name:"):
            result["name"] = line.split(":", 1)[1].strip()

        elif lower_line.startswith("document number:"):
            result["document_number"] = (
                line.split(":", 1)[1].strip()
            )

        elif lower_line.startswith("expiry:"):
            result["expiry_date"] = (
                line.split(":", 1)[1].strip()
            )

    return result


def process_document(image_path: str) -> Dict[str, Any]:
    """
    Complete OCR pipeline.
    """

    text = extract_text(image_path)

    fields = extract_document_fields(text)

    return {
        "success": True,
        "fields": fields
    }