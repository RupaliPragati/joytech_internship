from datetime import datetime, timezone

from fastapi import APIRouter

from app.core.config import settings
from app.ml.model_loader import model_loader

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():
    """
    Health monitoring endpoint.
    Reports API status, model status,
    backend version and current timestamp.
    """

    model_loaded = model_loader.get_model() is not None

    return {
        "api_status": "healthy",
        "model_loaded": model_loaded,
        "backend_version": settings.VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }