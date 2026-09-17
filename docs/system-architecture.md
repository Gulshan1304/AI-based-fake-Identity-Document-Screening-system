# System Architecture

## AI-Based Identity and Document Screening System

## 1. Overview

The system is designed as an AI-assisted platform for screening identity documents and identifying indicators that may require additional verification.

The architecture separates the frontend, backend API, AI/ML services, database, and human review layer.

---

# 2. High-Level Architecture

```text
                         USER
                           |
                           v
                +---------------------+
                |    React Frontend   |
                |                     |
                | Upload Document     |
                | Dashboard           |
                | History             |
                | Alerts              |
                | Admin Panel         |
                +----------+----------+
                           |
                           | REST API
                           v
                +---------------------+
                |    FastAPI Backend  |
                |                     |
                | API Routes          |
                | Validation          |
                | Authentication      |
                +----------+----------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        +---------+   +---------+   +---------+
        |   OCR   |   |  Face   |   | Tamper  |
        | Service |   | Verify  |   |Detection|
        +---------+   +---------+   +---------+
             |             |             |
             +-------------+-------------+
                           |
                           v
                +---------------------+
                | Anomaly Detection    |
                +----------+----------+
                           |
                           v
                +---------------------+
                |    Risk Engine      |
                |                     |
                | Score               |
                | Reason Codes        |
                +----------+----------+
                           |
                           v
                +---------------------+
                |      Database       |
                |                     |
                | Documents           |
                | Screenings          |
                | Alerts              |
                | Officer Reviews     |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   Officer Review    |
                |                     |
                | Review AI indicators|
                | Record decision     |
                +---------------------+
```

---

# 3. Frontend Layer

Technology:

```text
React.js
JavaScript
CSS
HTML
```

Responsibilities:

* Document upload
* Dashboard
* Screening results
* Risk score display
* Document history
* Alerts
* Watchlist interface
* Admin interface
* Officer review interface

---

# 4. Backend Layer

Technology:

```text
Python
FastAPI
Pydantic
SQLAlchemy
```

Responsibilities:

* Receive API requests
* Validate input
* Manage screening workflow
* Connect AI services
* Store results
* Manage alerts
* Provide admin APIs
* Connect frontend and database

---

# 5. AI/ML Layer

## OCR

Extracts text and structured information from supported documents.

Example fields:

```text
Name
Document Number
Date of Birth
Expiry Date
Address
```

---

## Face Verification

When an authorized workflow provides a comparison image, the system can compare the document portrait with that image and return a verification indicator.

---

## Tamper Detection

Analyzes document data or images for indicators of possible modification.

Examples of indicators:

```text
Text inconsistency
Image inconsistency
Layout anomaly
Unexpected metadata
```

---

## Anomaly Detection

Checks for unusual or inconsistent information.

Examples:

```text
Missing fields
Inconsistent dates
Unexpected document format
Data mismatch
```

---

# 6. Decision Layer

The decision layer combines screening outputs.

```text
AI Checks
   |
   v
Risk Engine
   |
   +--> Risk Score
   |
   +--> Risk Level
   |
   +--> Reason Codes
   |
   v
Review Recommendation
```

The system should preserve the underlying indicators so that a reviewer can understand why additional review was recommended.

---

# 7. Database Layer

Development database:

```text
SQLite
```

ORM:

```text
SQLAlchemy
```

Main entities:

```text
documents
screenings
alerts
officer_reviews
```

---

# 8. Human Review Layer

AI screening is separated from the final authorized decision.

```text
Document
   ↓
AI Screening
   ↓
Indicators
   ↓
Risk Assessment
   ↓
Officer Review
   ↓
Authorized Decision
```

This design helps prevent an automated model output from being treated as the final identity determination.

---

# 9. Security Layer

Planned security controls:

* Authentication
* Role-based access control
* Secure API endpoints
* Input validation
* Secure file handling
* Environment variables
* HTTPS
* Audit logging
* Access logging
* Data retention controls

---

# 10. Project Structure

```text
ai-identity-document-screening/
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── App.jsx
│       └── main.jsx
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── config.py
│       │
│       ├── api/
│       ├── models/
│       ├── services/
│       └── database/
│
├── ml/
│   ├── ocr/
│   ├── face_verification/
│   ├── tamper_detection/
│   └── anomaly_detection/
│
└── docs/
    ├── api_document.md
    ├── research.md
    └── system-architecture.md
```

---

# 11. Data Flow

```text
1. User uploads document
          ↓
2. Frontend sends document to API
          ↓
3. Backend validates request
          ↓
4. OCR extracts information
          ↓
5. Document checks are performed
          ↓
6. Anomaly indicators are generated
          ↓
7. Risk engine generates score/reason codes
          ↓
8. Result is stored
          ↓
9. Result displayed in dashboard
          ↓
10. Officer reviews when required
```

---

# 12. Deployment Architecture

Future production architecture:

```text
User
 |
 v
Web Application
 |
 v
HTTPS / API Gateway
 |
 v
FastAPI Backend
 |
 +---- AI/ML Services
 |
 +---- Database
 |
 +---- Audit Logs
 |
 v
Authorized Review Interface
```

Production deployment should use appropriate authentication, encryption, access control, monitoring, and privacy safeguards.
