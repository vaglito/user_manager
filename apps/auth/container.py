from apps.auth.infrastructure.repositories.auth_repository import SQLAlchemyAuthRepository
from apps.auth.infrastructure.services.jwt_service import JWTService
from apps.auth.application.commands.login_user import LoginUserUseCase

class AuthContainer:
    """
    Dependency Injection Container for the Auth context.

    This class wires together the necessary dependencies for the authentication logic,
    such as the authentication repository and the JWT service. It exposes the
    `LoginUserUseCase` as the main use case for handling user login.

    Attributes:
        auth_repository (SQLAlchemyAuthRepository): Concrete implementation of the AuthRepositoryPort
            used for validating user credentials via SQLAlchemy.
        jwt_service (JWTService): Service responsible for generating and verifying JWT tokens.
        login_user_use_case (LoginUserUseCase): Use case that handles user authentication by
            validating credentials and issuing a JWT.
    """

    def __init__(self):
        """
        Initialize the AuthContainer by instantiating the required services and use cases.
        """
        self.auth_repository = SQLAlchemyAuthRepository()
        self.jwt_service = JWTService()
        self.login_user_use_case = LoginUserUseCase(
            self.auth_repository,
            self.jwt_service
        )
