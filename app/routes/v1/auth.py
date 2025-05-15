from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from app.db.mongo import user_collection
from app.db.models.users import UsersCollection
from app.utils.auth import verify_password, create_access_token, hash_password
from app.schemas.auth_schema import UserRegister #UserRegisterResoponse
from typing import Dict
from datetime import datetime
from app.controllers import auth_ctrl
router = APIRouter()

@router.post("/register")
async def register(user: UserRegister):

    info = await auth_ctrl.register(user)
    print(info)
    return info
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # print(form_data.username)

    # data = {
    #     "username": form_data.username,
    #     "password": form_data.password
    # }
    info = await auth_ctrl.login(form_data)
    return info
