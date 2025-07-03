from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    email: str
    password: str
    first_name: str
    last_name: str
    uuid: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True
    updated_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)

