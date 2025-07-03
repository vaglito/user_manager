from fastapi import APIRouter, HTTPException
from apps.users.infrastructure.repositories import SQLAlchemyUserRepository
from apps.users.infrastructure.schemas import UserResponseSchema

router = APIRouter()

@router.get('/users/{user_uuid}', response_model=UserResponseSchema)
def get_user(user_uuid: str):
    repo = SQLAlchemyUserRepository()
    user = repo.get_by_id(user_uuid)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    return user

