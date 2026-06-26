import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "CERT-SAT Backend"
    VERSION = "1.0.0"

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

settings = Settings()