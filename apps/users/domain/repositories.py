from abc import ABC, abstractmethod
from .entities import User

class UserRepositoryPort(ABC):
    """
    Abstract base class (Port) for user repository.

    This interface defines the operations that any concrete user repository
    (e.g., SQLAlchemy, MongoDB, in-memory) must implement in the infrastructure layer.
    """

    @abstractmethod
    def create(self, user: User) -> User:
        """
        Persist a new user entity.

        Args:
            user (User): The user entity to be created.

        Returns:
            User: The created user with generated fields (e.g., uuid).
        """
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> User | None:
        """
        Retrieve a user by their UUID.

        Args:
            user_id (str): The UUID of the user.

        Returns:
            Optional[User]: The user entity if found, otherwise None.
        """
        pass

    @abstractmethod
    def get_by_email(self, user_email: str) -> User | None:
        pass