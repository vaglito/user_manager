
class UserAlreadyExistsException(Exception):
    """
    Raised when attempting to create a user with an email that already exists.

    Attributes:
        email (str): The email address that triggered the exception.
    """

    def __init__(self, email: str):
        self.email = email
        message = f"User with email '{email}' already exists."
        super().__init__(message)