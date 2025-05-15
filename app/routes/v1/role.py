from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from app.db.mongo import user_collection
from app.db.models.users import UserCollection
from app.utils.auth import verify_password, create_access_token, hash_password
from app.schemas.auth_schema import UserRegister, UserRegisterResoponse
from typing import Dict
from datetime import datetime
from app.controllers import role_ctrl
router = APIRouter()

@router.post("/add-role")
async def add_role(form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str,str]:
    info = await role_ctrl.add_role(form_data)
    return info

