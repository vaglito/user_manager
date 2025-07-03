from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, Field
from typing import Optional

class UserBaseSchema(BaseModel):
    """
    Base schema containing common user fields.
    This schema is used as a parent for other user-related schemas
    to ensure consistency and reuse.
    
    Fields:
        email (EmailStr): User's email address (validated format).
        first_name (Optional[str]): User's first name.
        last_name (Optional[str]): User's last name.
        phone (Optional[str]): User's phone number (max 20 characters).
    """
    email : EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = Field(default=None, max_length=20)


class UserCreateSchema(UserBaseSchema):
    """
    Schema used when creating a new user.
    Inherits fields from UserBaseSchema and adds the required password.

    Fields:
        password (str): User's password with validation constraints.
    """
    password: str = Field(..., min_length=8, max_length=255)


class UserUpdateSchema(BaseModel):
    """
    Schema used for updating user data.
    All fields are optional, allowing partial updates.

    Fields:
        email (Optional[EmailStr]): New email address.
        password (Optional[str]): New password (min 8, max 255 characters).
        first_name (Optional[str]): New first name.
        last_name (Optional[str]): New last name.
        phone (Optional[str]): New phone number (max 20 characters).
    """
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8, max_length=255)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[constr(max_length=20)] = None # type: ignore


class UserResponseSchema(UserBaseSchema):
    """
    Schema used to return user data from the API.
    Includes metadata fields such as uuid, created_at, and updated_at.

    Fields:
        uuid (UUID): Unique identifier for the user.
        created_at (datetime): Timestamp of when the user was created.
        updated_at (datetime): Timestamp of the last update to the user.
    """
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable compatibility with ORM models