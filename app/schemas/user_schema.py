from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, description="Full name of the user")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="Password (minimum 6 characters)")
    confirm_password: str = Field(..., min_length=6, description="Password confirmation")
    organization_email: Optional[EmailStr] = Field(None, description="Email of the organization")
    organization_country: Optional[str] = Field(None, description="Country of the organization")
    custom_fields: Optional[Dict[str, Any]] = Field(default_factory=dict)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)



class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str
    custom_fields: Optional[Dict[str, Any]] = {}



