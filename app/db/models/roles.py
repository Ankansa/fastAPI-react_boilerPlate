

from beanie import Document
from pydantic import Field
from datetime import datetime
from typing import Optional

class RolesCollection(Document):
    name: str = Field(...)
    guard_name: str = Field(...)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "roles"  
        indexes = ["name", "guard_name"]
