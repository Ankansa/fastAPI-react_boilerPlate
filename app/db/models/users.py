from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCollection(Document):
    name: str
    email: EmailStr
    password_hash: str
    role: str
    organization_name: str
    organization_country: str
    custom_fields: Optional[dict] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    

    class Settings:
        name = "users"  # Name of the MongoDB collection
        indexes = [
            "email",  # Index on the email field
            "created_at",  # Index on the created_at field
        ]
