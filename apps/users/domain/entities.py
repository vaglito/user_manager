from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    # auth fields
    uuid: Optional[str] = None
    email: str
    password: str

    # personal data
    first_name = str
    last_name = str
    phone: Optional[str] = None

    # Account State
    is_active: bool = True

    # time
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)

