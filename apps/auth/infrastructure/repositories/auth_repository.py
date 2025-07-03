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

        if user:
            print("👉 Email ingresado:", credentials.email)
            print("👉 Contraseña ingresada:", credentials.password)
            print("👉 Contraseña almacenada:", user.password)

            password_check = bcrypt.checkpw(credentials.password.encode(), user.password.encode())
            print("🔐 ¿Contraseña válida?", password_check)

            if password_check:
                return User(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    password=user.password,
                )

        return None