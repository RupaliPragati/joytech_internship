from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.auth import AuthService

router = APIRouter(tags=["Authentication"])

auth_service = AuthService()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = auth_service.authenticate(
        form_data.username,
        form_data.password,
    )

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return token