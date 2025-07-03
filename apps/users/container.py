from apps.users.infrastructure.repositories import SQLAlchemyUserRepository
from apps.users.application.commands.create_user import CreateUserUseCase
from apps.users.application.queries.get_user import GetUserByIdUseCase

class UsersContainer:
    def __init__(self):
        self.user_respository = SQLAlchemyUserRepository()
        self.create_user_use_case = CreateUserUseCase(self.user_respository)
        self.get_user_use_case = GetUserByIdUseCase(self.user_respository)