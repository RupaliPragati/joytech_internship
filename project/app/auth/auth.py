from app.auth.jwt_handler import create_access_token


class AuthService:

    def authenticate(
        self,
        username: str,
        password: str,
    ):

        # Temporary demo credentials
        if username == "admin" and password == "admin123":

            token = create_access_token(
                {"sub": username}
            )

            return {
                "access_token": token,
                "token_type": "bearer",
            }

        return None