from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    organization_name: Optional[str] = None
    organization_country: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = {}

class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str
    custom_fields: Optional[Dict[str, Any]] = {}



