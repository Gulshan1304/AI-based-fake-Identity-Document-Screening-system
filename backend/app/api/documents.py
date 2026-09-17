from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)


# Demo document database
documents = []


@router.get("/")
def get_documents():
    """
    Return document screening history.
    """

    return {
        "count": len(documents),
        "documents": documents
    }


@router.get("/{document_id}")
def get_document(document_id: str):
    """
    Get a specific document record.
    """

    for document in documents:

        if document["document_id"] == document_id:
            return document

    return {
        "document_id": document_id,
        "status": "NOT_FOUND",
        "message": "Document record not found."
    }


@router.post("/")
def create_document(document_data: dict):
    """
    Create a document record.
    """

    document_id = f"DOC-{len(documents) + 1:04d}"

    document = {
        "document_id": document_id,
        "document_type": document_data.get(
            "document_type",
            "UNKNOWN"
        ),
        "status": "PENDING",
        "created_at": datetime.utcnow().isoformat()
    }

    documents.append(document)

    return {
        "message": "Document record created.",
        "document": document
    }


@router.delete("/{document_id}")
def delete_document(document_id: str):
    """
    Delete a document record.
    """

    for document in documents:

        if document["document_id"] == document_id:

            documents.remove(document)

            return {
                "message": "Document record deleted.",
                "document_id": document_id
            }

    return {
        "document_id": document_id,
        "message": "Document not found."
    }