from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DocumentBase(BaseModel):
    document_type: str = Field(
        ...,
        description="Type of identity document"
    )

    document_number: Optional[str] = Field(
        default=None,
        description="Document identification number"
    )

    holder_name: Optional[str] = Field(
        default=None,
        description="Name extracted from document"
    )


class DocumentCreate(DocumentBase):
    """
    Data required when creating a document record.
    """
    pass


class Document(DocumentBase):
    """
    Complete document record.
    """

    document_id: str
    status: str = "PENDING"
    created_at: datetime

    class Config:
        from_attributes = True