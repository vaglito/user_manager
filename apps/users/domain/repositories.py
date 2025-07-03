from abc import ABC, abstractmethod
from .entities import User

class UserRepositoryPort(ABC):
    
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> User | None:
        pass