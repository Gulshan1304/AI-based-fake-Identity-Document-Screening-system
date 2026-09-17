from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings


DATABASE_URL = settings.DATABASE_URL


# SQLite database connection
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# Database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for database models
Base = declarative_base()


def get_db():
    """
    Create a database session
    and close it after the request.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def create_tables():
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)