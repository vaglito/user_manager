from fastapi import APIRouter, HTTPException
from apps.auth.domain.entities import AuthCredentials
from apps.auth.application.commands.login_user import LoginUserUseCase
from apps.container import container

router = APIRouter(prefix="/auth")


@router.post('/login/')
def login(credentials: AuthCredentials):
    repo = container.auth.auth_repository
    jwt_service = container.auth.jwt_service
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
