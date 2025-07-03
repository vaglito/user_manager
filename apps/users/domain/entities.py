from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    """
    Domain entity representing a User in the system.

    Attributes:
        email (str): User's email address (used for authentication).
        password (str): User's hashed password.
        first_name (str): User's first name.
        last_name (str): User's last name.
        uuid (Optional[UUID]): Unique identifier for the user (optional at creation).
        phone (Optional[str]): User's phone number (optional).
        is_active (bool): Flag indicating whether the user account is active.
        updated_at (datetime): Timestamp of last update.
        created_at (datetime): Timestamp when the user was created.
    """
    email: str
    password: str
    first_name: str
    last_name: str
    uuid: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)

