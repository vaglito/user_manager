from abc import ABC, abstractmethod
from apps.auth.domain.entities import AuthCredentials
from apps.users.domain.entities import User

class AuthRepositoryPort(ABC):
    """
    Abstract Base Class (Port) that defines the contract for authentication repositories.

    This interface must be implemented by any infrastructure class that handles
    authentication logic, such as verifying credentials against a database.

    Methods:
        authenticate(credentials: AuthCredentials) -> User | None:
            Given a set of authentication credentials, attempts to authenticate
            the user and return the corresponding User entity if successful.
            Returns None if authentication fails.
    """

    @abstractmethod
    def authenticate(self, credentials: AuthCredentials) -> User | None:
        """
        Attempt to authenticate a user with the provided credentials.

        Args:
            credentials (AuthCredentials): The credentials containing the user's email and password.

        Returns:
            User | None: The authenticated User entity if credentials are valid, otherwise None.
        """
        pass
