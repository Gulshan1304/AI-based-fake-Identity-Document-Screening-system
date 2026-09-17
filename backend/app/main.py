from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import screening
from app.api import documents
from app.api import alerts
from app.api import admin

from app.database.database import create_tables
from app.database import db_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables when the application starts
    create_tables()

    yield


app = FastAPI(
    title="AI Identity & Document Screening System",
    description="AI-assisted identity and document screening API",
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(screening.router)
app.include_router(documents.router)
app.include_router(alerts.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {
        "system": "AI Identity & Document Screening System",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }