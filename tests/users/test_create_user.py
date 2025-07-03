from apps.users.application.commands.create_user import CreateUserCommand, CreateUserUseCase
from apps.users.infrastructure.repositories import SQLAlchemyUserRepository

def test_create_user():
    repo = SQLAlchemyUserRepository()
    use_case = CreateUserUseCase(repo)
    cmd = CreateUserCommand(
        email='cesartest@gmail.com',
        password='TestpassWord!123.',
        first_name='Cesar',
        last_name='Gonzalez',
        phone='999888777'
    )
    user = use_case.execute(cmd)
    assert user.id is not None