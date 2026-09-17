from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AI Identity & Document Screening System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # API
    API_PREFIX: str = "/api"

    # File Upload
    MAX_FILE_SIZE_MB: int = 10

    # Database
    DATABASE_URL: str = "sqlite:///./screening.db"

    # CORS
    FRONTEND_URL: str = "http://localhost:5173"

    # Security
    SECRET_KEY: str = "change-this-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()