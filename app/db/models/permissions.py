from typing import Dict
from beanie import Document
from pydantic import BaseModel, Field
from bson import ObjectId

class PermissionsCollection(Document):
    user_id: str  # or ObjectId if you're using ObjectId
    permissions: Dict[str, bool] = Field(default_factory=dict)

    class Settings:
        name = "permissions"  # your MongoDB collection name
        indexes = [
            [("user_id", 1)],  # Create an index on user_id
        ]