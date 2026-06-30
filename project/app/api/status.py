from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {
        "backend": "running",
        "version": "1.0.0"
    }