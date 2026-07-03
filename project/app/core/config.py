import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    APP_NAME = "CERT-SAT Backend"
    VERSION = "1.0.0"

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    DATABASE_URL = os.getenv("DATABASE_URL")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0")

settings = Settings()