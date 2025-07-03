import bcrypt
from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from apps.users.domain.entities import User
from apps.users.domain.repositories import UserRepositoryPort
from apps.users.domain.exceptions import UserAlreadyExistsException

class CreateUserCommand(BaseModel):
    """
    Data Transfer Object (DTO) for creating a user.

    Validates the input data before executing the use case.
    """
    email: EmailStr
    password: constr(min_length=8, max_length=255)  # type: ignore
    first_name: str
    last_name: str
    phone: Optional[str] = None

class CreateUserUseCase:
    """
    Use case responsible for handling the user creation logic.

    Steps:
    1. Check if email already exists.
    2. Hash password using bcrypt with salt.
    3. Create the User entity.
    4. Persist the user using the repository.
    """
    def __init__(self, repo: UserRepositoryPort):
        """
        Constructor for dependency injection of the user repository.

        :param repo: An implementation of UserRepositoryPort
        """
        self.repo = repo

    def execute(self, command: CreateUserCommand) -> User:
        """
        Executes the CreateUser command.

        :param command: CreateUserCommand containing validated user data
        :raises UserAlreadyExistsException: if email is already registered
        :return: The persisted User entity
        """
        # Check if user with the given email already exists
        existing_user = self.repo.get_by_email(command.email)
        if existing_user:
            raise UserAlreadyExistsException(command.email)
        
        # Securely hash the password using bcrypt with salt
        hashed_pw = bcrypt.hashpw(
            command.password.encode(),
            bcrypt.gensalt()).decode(
        )
        
        user = User(
            uuid=None,
            email=command.email,
            password=hashed_pw,
            first_name=command.first_name,
            last_name=command.last_name,
            phone=command.phone,
            is_active=True,
        )
        return self.repo.create(user)