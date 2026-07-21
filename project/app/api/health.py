from datetime import datetime, timezone

from fastapi import APIRouter

from app.core.config import settings
from app.ml.model_loader import model_loader

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
    description="Returns the current health status of the backend, ML model availability, backend version, and current UTC timestamp.",
    responses={
        200: {
            "description": "Backend is healthy",
            "content": {
                "application/json": {
                    "example": {
                        "api_status": "healthy",
                        "model_loaded": True,
                        "backend_version": "1.0.0",
                        "timestamp": "2026-07-21T15:00:00+00:00"
                    }
                }
            }
        }
    }
)
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