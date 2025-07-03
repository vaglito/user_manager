from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError # type: ignore
from decouple import config
from apps.users.domain.entities import User
from apps.auth.infrastructure.repositories.auth_repository import SQLAlchemyAuthRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM", default="HS256")

def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> User:
    """
    Extract the current user from the JWT token.

    Args:
        token (str): The JWT token from the Authorization header.

    Returns:
        User: The user associated with the decoded token.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    # Get the user from the database (repository)
    repo = SQLAlchemyAuthRepository()
    user = repo.get_user_by_email(email=email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user
