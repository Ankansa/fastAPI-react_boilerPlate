from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from app.db.mongo import user_collection
from app.db.models.users import UserCollection
from app.utils.auth import verify_password, create_access_token, hash_password
from app.schemas.auth_schema import UserRegister, UserRegisterResoponse
from typing import Dict
from datetime import datetime

async def add_role(form_data):
    try:
        user = await UserCollection.find_one({"email": form_data.username})

        if user:
            user = user.model_dump()

        if not user or not verify_password(form_data.password, user["password_hash"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": str(user["id"]), "role": user["role"]})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        print(f"Error in login_ctrl: {e}")
        return {"access_token": None, "token_type": "Unable to generate token"}

