from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.database import Base


# =========================================================
# DOCUMENT TABLE
# =========================================================

class DocumentDB(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    document_type = Column(
        String,
        nullable=False
    )

    document_number = Column(
        String,
        nullable=True
    )

    holder_name = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    screenings = relationship(
        "ScreeningDB",
        back_populates="document"
    )


# =========================================================
# SCREENING TABLE
# =========================================================

class ScreeningDB(Base):

    __tablename__ = "screenings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    screening_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=True
    )

    status = Column(
        String,
        default="PENDING"
    )

    risk_score = Column(
        Integer,
        nullable=True
    )

    risk_level = Column(
        String,
        nullable=True
    )

    reason_codes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    document = relationship(
        "DocumentDB",
        back_populates="screenings"
    )

    officer_reviews = relationship(
        "OfficerReviewDB",
        back_populates="screening"
    )


# =========================================================
# OFFICER REVIEW TABLE
# =========================================================

class OfficerReviewDB(Base):

    __tablename__ = "officer_reviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    review_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    screening_id = Column(
        Integer,
        ForeignKey("screenings.id"),
        nullable=False
    )

    officer_id = Column(
        String,
        nullable=False
    )

    decision = Column(
        String,
        nullable=False
    )

    remarks = Column(
        Text,
        nullable=True
    )

    reviewed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    screening = relationship(
        "ScreeningDB",
        back_populates="officer_reviews"
    )


# =========================================================
# ALERT TABLE
# =========================================================

class AlertDB(Base):

    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    alert_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    alert_type = Column(
        String,
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    severity = Column(
        String,
        default="MEDIUM"
    )

    status = Column(
        String,
        default="OPEN"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )