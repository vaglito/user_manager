from apps.auth.infrastructure.repositories.auth_repository import SQLAlchemyAuthRepository
from apps.auth.infrastructure.services.jwt_service import JWTService
from apps.auth.application.commands.login_user import LoginUserUseCase

class AuthContainer:
    def __init__(self):
        self.auth_repository = SQLAlchemyAuthRepository()
        self.jwt_service = JWTService()
        self.login_user_use_case = LoginUserUseCase(
            self.auth_repository,
            self.jwt_service
        )