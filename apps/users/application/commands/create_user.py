import bcrypt
from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from apps.users.domain.entities import User
from apps.users.domain.repositories import UserRepositoryPort

class CreateUserCommand(BaseModel):
    """
    Command object for creating a user.
    """
    email: EmailStr
    password: constr(min_length=8, max_length=255)  # type: ignore
    first_name: str
    last_name: str
    phone: Optional[str] = None

class CreateUserUseCase:
    def __init__(self, repo: UserRepositoryPort):
        self.repo = repo

    def execute(self, command: CreateUserCommand) -> User:
        hashed_pw = bcrypt.hashpw(command.password.encode(), bcrypt.gensalt()).decode()
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