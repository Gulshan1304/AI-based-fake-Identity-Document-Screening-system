# AI Identity & Document Screening System — Backend

## 📌 Overview

This is the backend API for the **AI-Based Identity and Document Screening System**.

The backend is built with **Python and FastAPI** and is responsible for receiving documents, managing screening requests, generating screening results, maintaining document history, handling alerts, and providing admin APIs.

> **Note:** This project is an AI-assisted screening prototype. Screening results are indicators for review and should not independently determine a person's identity or legal status.

---

## 🛠️ Technology Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLite (development)
* REST API
* OCR
* Face Verification
* Tamper Detection
* Anomaly Detection
* Risk Scoring

---

## 📁 Backend Structure

```text
backend/
│
├── app/
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── alerts.py
│   │   ├── documents.py
│   │   └── screening.py
│   │
│   ├── services/
│   │   ├── ocr_service.py
│   │   ├── face_verification.py
│   │   ├── tamper_detection.py
│   │   ├── anomaly_detection.py
│   │   ├── risk_engine.py
│   │   └── reason_codes.py
│   │
│   ├── models/
│   │   ├── document.py
│   │   ├── screening.py
│   │   └── officer_review.py
│   │
│   └── database/
│       ├── database.py
│       └── crud.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Open the backend folder

```bash
cd backend
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 API Endpoints

## 1. Health Check

### GET

```text
/health
```

Checks whether the backend is running.

Example response:

```json
{
  "status": "healthy"
}
```

---

## 2. Document Screening

### POST

```text
/api/screening/
```

Used to upload a document and start AI-assisted screening.

The screening pipeline is designed to include:

```text
Document
   ↓
OCR
   ↓
Document Authentication
   ↓
Tamper Detection
   ↓
Face Verification
   ↓
Expiry Validation
   ↓
Watchlist Screening
   ↓
Anomaly Detection
   ↓
Risk Engine
   ↓
Screening Result
   ↓
Human Review
```

---

## 3. Document History

### GET

```text
/api/documents/
```

Returns document screening records.

### GET

```text
/api/documents/{document_id}
```

Returns a specific document record.

### POST

```text
/api/documents/
```

Creates a document record.

### DELETE

```text
/api/documents/{document_id}
```

Deletes a document record.

---

## 4. Alerts

### GET

```text
/api/alerts/
```

Returns generated screening alerts.

### POST

```text
/api/alerts/
```

Creates an alert.

### PATCH

```text
/api/alerts/{alert_id}/resolve
```

Marks an alert as resolved.

---

## 5. Admin

### GET

```text
/api/admin/dashboard
```

Returns dashboard statistics.

### GET

```text
/api/admin/screenings
```

Returns screening records for the admin interface.

### GET

```text
/api/admin/system-status
```

Checks backend, database, and AI-service status.

---

# 🤖 AI Screening Services

The backend separates individual AI tasks into services.

### OCR

```text
ocr_service.py
```

Extracts text and structured fields from supported documents.

### Face Verification

```text
face_verification.py
```

Compares a document portrait with an authorized verification image when such a workflow is available.

### Tamper Detection

```text
tamper_detection.py
```

Looks for indicators of possible document modification.

### Anomaly Detection

```text
anomaly_detection.py
```

Checks for missing, inconsistent, or unusual document information.

### Risk Engine

```text
risk_engine.py
```

Combines screening indicators into a transparent risk score.

### Reason Codes

```text
reason_codes.py
```

Provides explanations for screening indicators, such as:

```text
DOC_TAMPER_INDICATOR
FACE_MISMATCH
DOCUMENT_EXPIRED
DATA_INCONSISTENCY
WATCHLIST_REVIEW
```

---

# 📊 Screening Status

The system can return statuses such as:

```text
VERIFIED
REVIEW_REQUIRED
PENDING
FAILED
EXPIRED
```

Example:

```json
{
  "status": "REVIEW_REQUIRED",
  "risk": {
    "score": 35,
    "level": "LOW",
    "reason_codes": [
      "DATA_INCONSISTENCY"
    ]
  }
}
```

The risk score is an **AI-assisted screening indicator**, not a final determination.

---

# 🔐 Security

The backend should eventually include:

* Authentication
* Role-based access control
* Secure file handling
* Input validation
* HTTPS in production
* Environment variables for secrets
* Database access controls
* Audit logs
* Access logging
* Data retention policies
* Privacy protections

Sensitive credentials and secret keys should never be committed to GitHub.

---

# 🌐 Frontend Connection

The React frontend communicates with the FastAPI backend through REST APIs.

Development architecture:

```text
React Frontend
      │
      │ HTTP / REST
      ▼
FastAPI Backend
      │
      ├── Screening APIs
      ├── Document APIs
      ├── Alert APIs
      └── Admin APIs
             │
             ▼
       AI Services
             │
             ▼
          Database
```

Frontend development server:

```text
http://localhost:5173
```

Backend development server:

```text
http://127.0.0.1:8000
```

---

# 🧪 Development Status

| Module              | Status         |
| ------------------- | -------------- |
| FastAPI Server      | ✅              |
| API Structure       | ✅              |
| Document API        | ✅              |
| Screening API       | ✅              |
| Alert API           | ✅              |
| Admin API           | ✅              |
| Configuration       | ✅              |
| Database            | 🔄 Development |
| OCR                 | 🔄 Development |
| Face Verification   | 🔄 Development |
| Tamper Detection    | 🔄 Development |
| Anomaly Detection   | 🔄 Development |
| Risk Engine         | 🔄 Development |
| Authentication      | 🔄 Planned     |
| Production Security | 🔄 Planned     |

---

# 🎯 Future Improvements

* Connect React frontend with FastAPI
* Implement real OCR pipeline
* Add document-field extraction
* Add authorized face-verification workflow
* Improve tamper-indicator detection
* Add anomaly detection
* Connect risk engine
* Add database persistence
* Add officer review workflow
* Add audit logging
* Add authentication and authorization
* Add automated testing
* Containerize with Docker

---

## 👨‍💻 Project

**AI-Based Identity and Document Screening System**

**Backend:** Python + FastAPI

**Purpose:** AI-assisted document and identity screening with explainable indicators and human review.
