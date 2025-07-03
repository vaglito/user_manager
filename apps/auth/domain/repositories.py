from abc import ABC, abstractmethod
from apps.auth.domain.entities import AuthCredentials
from apps.users.domain.entities import User

class AuthRepositoryPort(ABC):

    @abstractmethod
    def authenticate(self, credentials: AuthCredentials) -> User | None:
        pass