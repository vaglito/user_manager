import bcrypt
from apps.auth.domain.repositories import AuthRepositoryPort
from apps.auth.domain.entities import AuthCredentials
from apps.users.infrastructure.models import UserModel
from apps.users.domain.entities import User
from config.db import SessionLocal

class SQLAlchemyAuthRepository(AuthRepositoryPort):
    """
    Concrete implementation of the AuthRepositoryPort using SQLAlchemy ORM.

    This repository handles the logic for authenticating a user by checking
    the provided credentials against the database.

    Methods:
        authenticate(credentials: AuthCredentials) -> User | None:
            Validates the email and password against the stored user.
    """

    def authenticate(self, credentials: AuthCredentials) -> User | None:
        """
        Authenticate a user by verifying their email and password.

        Args:
            credentials (AuthCredentials): Object containing the user's email and password.

        Returns:
            User | None: Returns a User domain entity if authentication is successful,
                         otherwise returns None.
        """
        session = SessionLocal()
        user = session.query(UserModel).filter_by(email=credentials.email).first()
        session.close()

        if user:
            password_check = bcrypt.checkpw(credentials.password.encode(), user.password.encode())

            if password_check:
                return User(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    password=user.password,
                )

        return None
