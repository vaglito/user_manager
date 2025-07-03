from fastapi import APIRouter, HTTPException
from apps.auth.domain.entities import AuthCredentials
from apps.auth.infrastructure.repositories.auth_repository import SQLAlchemyAuthRepository
from apps.auth.infrastructure.services.jwt_service import JWTService
from apps.auth.application.commands.login_user import LoginUserUseCase

router = APIRouter(prefix="/auth")


@router.post('/login/')
def login(credentials: AuthCredentials):
    repo = SQLAlchemyAuthRepository()
    jwt_service = JWTService()
    use_case = LoginUserUseCase(repo, jwt_service)

    try:
        token = use_case.execute(credentials)
        return {
            "access_token": token
        }
    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials."
        )
