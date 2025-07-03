from apps.users.domain.entities import User
from apps.users.domain.repositories import UserRepositoryPort
from .models import UserModel
from config.db import SessionLocal


class SQLAlchemyUserRepository(UserRepositoryPort):
    def __init__(self):
        self.session = SessionLocal()

    def create(self, user: User) -> User:
        db_user = UserModel(
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return self._to_entity(db_user)

    def get_by_id(self, user_uuid: str) -> User | None:
        db_user = self.session.query(
            UserModel).filter_by(uuid=user_uuid).first()
        if db_user:
            return self._to_entity(db_user)
        return None

    def _to_entity(self, user_model: UserModel) -> User:
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
