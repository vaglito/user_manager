from apps.users.container import UsersContainer
from apps.auth.container import AuthContainer

class Container:
    def __init__(self):
        self.users = UsersContainer()
        self.auth = AuthContainer()

# Global instance
container = Container()