
from apps.users.domain.repositories import UserRepositoryPort


class GetUserByIdUseCase:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def execute(self, user_uuid: str):
        return self.repository.get_by_id(user_uuid)