from fastapi import APIRouter, HTTPException
from apps.container import container
from apps.users.infrastructure.schemas import UserResponseSchema

router = APIRouter()

@router.get('/users/{user_uuid}', response_model=UserResponseSchema)
def get_user(user_uuid: str):
    user = container.users.get_user_use_case.execute(user_uuid)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    return user

