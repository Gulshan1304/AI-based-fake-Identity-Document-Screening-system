from typing import Dict, Any, List
from datetime import datetime
import re


# ---------------------------------------------------------
# LICENSE NUMBER FORMAT
# ---------------------------------------------------------

def validate_license_number(
    document_number: str
) -> bool:
    """
    Basic format validation for a driving-license number.

    This checks format only.
    It does NOT prove that the license is genuine.
    """

    if not document_number:
        return False

    document_number = document_number.strip()

    # Basic alphanumeric format
    pattern = r"^[A-Za-z0-9/-]{6,25}$"

    return bool(
        re.fullmatch(pattern, document_number)
    )


# ---------------------------------------------------------
# DATE VALIDATION
# ---------------------------------------------------------

def validate_date(date_value: str) -> bool:
    """
    Check whether the supplied date can be parsed.
    """

    if not date_value:
        return False

    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d"
    ]

    for date_format in formats:

        try:
            datetime.strptime(
                date_value.strip(),
                date_format
            )

            return True

        except ValueError:
            continue

    return False


# ---------------------------------------------------------
# EXPIRY CHECK
# ---------------------------------------------------------

def check_expiry(expiry_date: str) -> str:
    """
    Check whether the license has expired.
    """

    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d"
    ]

    expiry = None

    for date_format in formats:

        try:

            expiry = datetime.strptime(
                expiry_date.strip(),
                date_format
            )

            break

        except ValueError:
            continue

    if expiry is None:
        return "INVALID_DATE"

    today = datetime.now()

    if expiry.date() < today.date():
        return "EXPIRED"

    return "VALID"


# ---------------------------------------------------------
# MAIN LICENSE VALIDATION
# ---------------------------------------------------------

def validate_license(
    data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Validate extracted license/document information.

    This is a screening rule, not an authenticity
    verification system.
    """

    reason_codes: List[str] = []

    name = data.get("name")
    document_number = data.get("document_number")
    expiry_date = data.get("expiry_date")

    # -----------------------------------------------------
    # Name
    # -----------------------------------------------------

    if not name or not str(name).strip():

        reason_codes.append(
            "MISSING_NAME"
        )

    elif len(str(name).strip()) < 2:

        reason_codes.append(
            "INVALID_NAME"
        )

    # -----------------------------------------------------
    # License Number
    # -----------------------------------------------------

    if not document_number:

        reason_codes.append(
            "MISSING_LICENSE_NUMBER"
        )

    elif not validate_license_number(
        str(document_number)
    ):

        reason_codes.append(
            "INVALID_LICENSE_NUMBER_FORMAT"
        )

    # -----------------------------------------------------
    # Expiry Date
    # -----------------------------------------------------

    if not expiry_date:

        reason_codes.append(
            "MISSING_EXPIRY_DATE"
        )

    elif not validate_date(
        str(expiry_date)
    ):

        reason_codes.append(
            "INVALID_EXPIRY_DATE"
        )

    else:

        expiry_status = check_expiry(
            str(expiry_date)
        )

        if expiry_status == "EXPIRED":

            reason_codes.append(
                "EXPIRED_DOCUMENT"
            )

    # -----------------------------------------------------
    # Final Status
    # -----------------------------------------------------

    if reason_codes:

        status = "REVIEW_REQUIRED"

    else:

        status = "VALIDATION_PASSED"

    return {
        "status": status,
        "valid": len(reason_codes) == 0,
        "reason_codes": reason_codes,
        "message": (
            "Document requires further review."
            if reason_codes
            else
            "Basic license validation checks passed."
        )
    }