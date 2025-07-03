from apps.users.domain.entities import User
from apps.users.domain.repositories import UserRepositoryPort
from .models import UserModel
from config.db import SessionLocal
from contextlib import contextmanager


class SQLAlchemyUserRepository(UserRepositoryPort):
    """
    SQLAlchemy implementation of the UserRepositoryPort.
    This repository handles persistence logic for User entities using SQLAlchemy.
    """

    @contextmanager
    def get_session(self):
        session = SessionLocal()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def create(self, user: User) -> User:
        """
        Persists a new user into the database.

        Args:
            user (User): The user entity to be created.

        Returns:
            User: The created user entity, with DB-generated fields.
        """
        with self.get_session() as session:
            db_user = UserModel(
                email=user.email,
                password=user.password,
                first_name=user.first_name,
                last_name=user.last_name,
                phone=user.phone
            )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return self._to_entity(db_user)

    def get_by_id(self, user_uuid: str) -> User | None:
        """
        Retrieves a user from the database by UUID.

        Args:
            user_uuid (str): The UUID of the user.

        Returns:
            Optional[User]: The corresponding User entity, or None if not found.
        """
        db_user = self.session.query(
            UserModel).filter_by(uuid=user_uuid).first()
        if db_user:
            return self._to_entity(db_user)
        return None

    def get_by_email(self, user_email: str) -> User | None:
        with self.get_session() as session:
            db_user = session.query(UserModel).filter_by(email=user_email).first()
            if db_user:
                return self._to_entity(db_user)
        return None

    def _to_entity(self, user_model: UserModel) -> User:
        """
        Maps a SQLAlchemy model instance to a domain User entity.

        Args:
            user_model (UserModel): The SQLAlchemy model.

        Returns:
            User: The domain entity.
        """
        return User(
            uuid=user_model.uuid,
            email=user_model.email,
            password=user_model.password,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            phone=user_model.phone,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at
        )
