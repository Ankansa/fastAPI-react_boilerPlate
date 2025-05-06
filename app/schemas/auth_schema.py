from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserRegisterResoponse(BaseModel):
    message: str
    user_id: str
    email: EmailStr

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    organization_name: str
    organization_country: str
    password: str
    custom_fields: Optional[Dict[str, Any]] = {}
    created_at: Optional[str] = datetime.utcnow().isoformat()
    updated_at: Optional[str] = datetime.utcnow().isoformat()