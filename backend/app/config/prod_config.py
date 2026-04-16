import os
from app.config.config import Config

class ProductionConfig(Config):
    DEBUG = False

    # PostgreSQL (Production)
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

    # File Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

    # Logging
    LOG_LEVEL = "INFO"