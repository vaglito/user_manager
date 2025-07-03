import bcrypt
from apps.auth.domain.repositories import AuthRepositoryPort
from apps.auth.domain.entities import AuthCredentials
from apps.users.infrastructure.models import UserModel
from apps.users.domain.entities import User
from config.db import SessionLocal

class SQLAlchemyAuthRepository(AuthRepositoryPort):
    def authenticate(self, credentials: AuthCredentials) -> User | None:
        session = SessionLocal()

        user = session.query(UserModel).filter_by(email=credentials.email).first()
        session.close()

        if user and bcrypt.checkpw(credentials.password.encode(), user.password.encode()):
            return User.from_orm(user)
        return None