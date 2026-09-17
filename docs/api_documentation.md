# API Documentation

## AI-Based Identity and Document Screening System

This document describes the REST APIs used by the AI-Based Identity and Document Screening System.

---

## Base URL

Development:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 1. Health API

## GET `/health`

Checks whether the backend is running.

### Response

```json
{
  "status": "healthy"
}
```

---

# 2. Screening API

## POST `/api/screening/`

Uploads a document and starts AI-assisted screening.

### Request

```text
Content-Type: multipart/form-data
```

Parameter:

```text
document: File
```

Supported file types:

```text
PDF
JPG
JPEG
PNG
```

### Example Response

```json
{
  "screening_id": "SCR-12345678",
  "filename": "identity-document.pdf",
  "status": "REVIEW_REQUIRED",
  "checks": {
    "document_authentication": "PENDING",
    "tamper_detection": "PENDING",
    "face_verification": "PENDING",
    "expiry_validation": "PENDING",
    "watchlist_screening": "PENDING",
    "anomaly_detection": "PENDING"
  },
  "risk": {
    "score": null,
    "level": "NOT_AVAILABLE",
    "reason_codes": []
  }
}
```

---

## GET `/api/screening/{screening_id}`

Returns information about a screening request.

### Example

```text
GET /api/screening/SCR-12345678
```

### Response

```json
{
  "screening_id": "SCR-12345678",
  "status": "REVIEW_REQUIRED",
  "message": "Screening result retrieved successfully."
}
```

---

# 3. Documents API

## GET `/api/documents/`

Returns document screening history.

### Response

```json
{
  "count": 2,
  "documents": [
    {
      "document_id": "DOC-0001",
      "document_type": "IDENTITY_DOCUMENT",
      "status": "PENDING"
    }
  ]
}
```

---

## GET `/api/documents/{document_id}`

Returns a specific document.

Example:

```text
GET /api/documents/DOC-0001
```

---

## POST `/api/documents/`

Creates a document record.

### Request

```json
{
  "document_type": "IDENTITY_DOCUMENT",
  "document_number": "DOCUMENT_NUMBER",
  "holder_name": "Example User"
}
```

---

## DELETE `/api/documents/{document_id}`

Deletes a document record.

---

# 4. Alerts API

## GET `/api/alerts/`

Returns screening alerts.

### Example Response

```json
{
  "count": 1,
  "alerts": [
    {
      "alert_id": "ALT-12345678",
      "alert_type": "DATA_INCONSISTENCY",
      "message": "Manual review recommended.",
      "severity": "MEDIUM",
      "status": "OPEN"
    }
  ]
}
``
```
