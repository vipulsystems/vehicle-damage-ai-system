import os
from app.config.config import Config

class DevelopmentConfig(Config):
    DEBUG = True

    # PostgreSQL (Dev)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "vehicle_ai")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

    # File Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

    # Optional: Logging level
    LOG_LEVEL = "DEBUG"