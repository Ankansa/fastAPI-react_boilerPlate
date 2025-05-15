from beanie import Document
from pydantic import Field
from beanie import PydanticObjectId

class RoleHasPermissionsCollection(Document):
    permission_id: PydanticObjectId = Field(...)
    role_id: PydanticObjectId = Field(...)

    class Settings:
        name = "role_has_permissions"  # MongoDB collection name
        indexes = ["permission_id", "role_id"]
