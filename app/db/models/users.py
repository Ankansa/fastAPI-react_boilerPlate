from beanie import Document
from pydantic import Field, EmailStr
from typing import Optional, Dict
from datetime import datetime

class UsersCollection(Document):
    name: str = Field(..., min_length=2, description="Full name of the user")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="Password (minimum 6 characters)")
    organization_email: Optional[EmailStr] = Field(None, description="Email of the organization")
    organization_country: Optional[str] = Field(None, description="Country of the organization")
    custom_fields: Optional[Dict] = {}
    created_by: Optional[str] = Field(None, description="User who created this user")
    isactive: bool = Field(default=True, description="Is the user active?")
    role: str = Field(default="admin", description="User role (admin/user)")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"  # MongoDB collection name
        indexes = ["email", "org_id", "role"]
