import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
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
