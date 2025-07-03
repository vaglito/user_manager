from pydantic import BaseModel, EmailStr

class AuthCredentials(BaseModel):
    """
    Data Transfer Object (DTO) for authentication credentials.

    This model is used to encapsulate the data required for a user to log in.
    It ensures that the provided email is valid and that both fields are present.

    Attributes:
        email (EmailStr): The user's email address. Must be a valid email format.
        password (str): The user's password in plain text.
    """
    email: EmailStr
    password: str
