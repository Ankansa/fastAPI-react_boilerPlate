from beanie import Document
from pydantic import Field, BaseModel
from datetime import datetime
from typing import Optional

class PermissionsCollection(Document):
    user_id: str = Field(..., description="Reference to the user ID")
    create_user: bool
    view_users: bool
    view_sales: bool
    permissions: Optional[dict] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "permissions"  # Name of the MongoDB collection
        indexes = [
            "user_id",  # Index on the user_id field
        ]
