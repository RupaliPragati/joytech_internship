from fastapi import APIRouter

from app.auth.firebase_auth import verify_google_token
from app.models.google_auth import GoogleLoginRequest

router = APIRouter(tags=["Authentication"])

@router.post("/google-login")
def google_login(request: GoogleLoginRequest):
    decoded = verify_google_token(request.id_token)

    return {
        "status": "success",
        "message": "Google authentication successful",
        "user": {
            "uid": decoded["uid"],
            "email": decoded.get("email"),
            "name": decoded.get("name"),
            "picture": decoded.get("picture"),
        },
    }