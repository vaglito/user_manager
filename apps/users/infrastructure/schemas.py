from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, Field
from typing import Optional

class UserBaseSchema(BaseModel):
    """
    Base schema with common user fields.
    """
    email : EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[constr(max_length=20)] = None # type: ignore


class UserCreateSchema(UserBaseSchema):
    """
    Schema for user creation.
    """
    password = constr(min_length=8, max_length=255)


class UserUpdateSchema(BaseModel):
    """
    Schema for updating user data.
    All fields are optional.
    """
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8, max_length=255)] = None # type: ignore
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[constr(max_length=20)] = None # type: ignore


class UserResponseSchema(UserBaseSchema):
    """
    Schema for returning user data.
    """
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable compatibility with ORM models