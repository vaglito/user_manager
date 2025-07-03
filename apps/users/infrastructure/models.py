import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

# Declarative base for SQLAlchemy ORM
Base = declarative_base()

class UserModel(Base):
    """
    SQLAlchemy model that maps to the 'users' table in the database.

    Fields:
        uuid (UUID): Primary key, uniquely identifies the user.
        email (str): Unique email address used for authentication and contact.
        password (str): Hashed password for authentication.
        first_name (str): User's first name.
        last_name (str): User's last name.
        phone (str): Optional phone number (max 20 characters).
        created_at (datetime): Timestamp when the user was created.
        updated_at (datetime): Timestamp of the last update.
    """
    __tablename__ = 'users'

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )
    email = Column(
        String(100),
        unique=True,
        nullable=False
    )
    password = Column(
        String(255),
        nullable=False
    )
    first_name = Column(
        String(50),
    )
    last_name = Column(
        String(50),
    )
    phone = Column(
        String(20),
        nullable=True
    )
    created_at = Column(
        DateTime,
        default=datetime.now
    )
    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
