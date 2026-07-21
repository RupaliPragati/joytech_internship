from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/status",
    tags=["Status"],
    summary="Backend Status",
    description="Returns the current operational status and version of the backend service.",
    responses={
        200: {
            "description": "Backend is running",
            "content": {
                "application/json": {
                    "example": {
                        "backend": "running",
                        "version": "1.0.0"
                    }
                }
            }
        }
    },
)
def status():
    return {
        "backend": "running",
        "version": "1.0.0"
    }