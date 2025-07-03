from apps.auth.domain.repositories import AuthRepositoryPort
from apps.auth.domain.entities import AuthCredentials
from apps.auth.infrastructure.services.jwt_service import JWTService


class LoginUseCase:
    def __init__(self, repo: AuthRepositoryPort, jwt_service: JWTService):
        self.repo = repo
        self.jwt_service = jwt_service

    def execute(self, credentials: AuthCredentials) -> str:
        user = self.repo.authenticate(credentials)
        if not user:
            raise ValueError('Invalid credentials.')
        return self.jwt_service.create_token(user)