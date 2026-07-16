from fastapi import APIRouter, HTTPException

from app.auth.auth import AuthService
from app.models.auth import LoginRequest

router = APIRouter(tags=["Authentication"])

auth_service = AuthService()


@router.post("/login")
def login(data: LoginRequest):

    token = auth_service.authenticate(
        data.username,
        data.password,
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return token