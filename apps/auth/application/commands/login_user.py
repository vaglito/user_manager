from apps.auth.domain.repositories import AuthRepositoryPort
from apps.auth.domain.entities import AuthCredentials
from apps.auth.infrastructure.services.jwt_service import JWTService

class LoginUserUseCase:
    """
    Application use case for logging in a user.

    This use case coordinates the authentication of a user by verifying credentials
    through the authentication repository and generating a JWT upon success.

    Attributes:
        repo (AuthRepositoryPort): Repository used to authenticate user credentials.
        jwt_service (JWTService): Service used to generate JWT tokens.
    
    Methods:
        execute(credentials: AuthCredentials) -> str:
            Authenticates the user and returns a JWT token if credentials are valid.
    """

    def __init__(self, repo: AuthRepositoryPort, jwt_service: JWTService):
        """
        Initialize the LoginUserUseCase.

        Args:
            repo (AuthRepositoryPort): The repository used to authenticate users.
            jwt_service (JWTService): The service used to create JWT tokens.
        """
        self.repo = repo
        self.jwt_service = jwt_service

    def execute(self, credentials: AuthCredentials) -> str:
        """
        Execute the login use case: authenticate user and return JWT.

        Args:
            credentials (AuthCredentials): The user's login credentials.

        Returns:
            str: JWT token if authentication is successful.

        Raises:
            ValueError: If credentials are invalid.
        """
        user = self.repo.authenticate(credentials)
        if not user:
            raise ValueError('Invalid credentials.')
        return self.jwt_service.create_token(user)
