from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.auth import AuthService

router = APIRouter(tags=["Authentication"])

auth_service = AuthService()


@router.post(
    "/login",
    summary="User Login",
    description="Authenticates a user and returns a JWT access token.",
    responses={
        200: {
            "description": "Login successful",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer"
                    }
                }
            },
        },
        401: {
            "description": "Invalid credentials",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid username or password"
                    }
                }
            },
        },
    },
)
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