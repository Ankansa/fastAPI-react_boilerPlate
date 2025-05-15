from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from app.db.mongo import user_collection
from app.db.models.users import UsersCollection
from app.utils.auth import verify_password, create_access_token, hash_password
from app.schemas.auth_schema import UserRegister
from typing import Dict
from datetime import datetime, timedelta

async def register(user: UserRegister):
    try:
        # Check if email is already registered
        if await UsersCollection.find_one({"email": user.email}):
            raise HTTPException(status_code=400, detail="Email already registered.")

        # Prepare user data

        user_data = {
            "name": user.name,
            "email": user.email,
            "password": hash_password(user.password),
            "organization_email": user.organization_email,
            "organization_country": user.organization_country,
            "custom_fields": {},
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
        

        # Create and insert the user
        new_user = UsersCollection(**user_data)
        result = await new_user.insert()

        

        return {
            "message": "Admin user created successfully",
            "user_id": str(result.id),
            "email": user.email
        }

    except Exception as e:
        print(f"Error in register: {e}")
        return {"message": "Unable to create user", "error": str(e)}
async def login(form_data):
    try:
        user = await UsersCollection.find_one({"email": form_data.username})

        if user:
            user = user.model_dump()

        if not user or not verify_password(form_data.password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": str(user["id"]), "role": user["role"]})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        print(f"Error in login_ctrl: {e}")
        return {"access_token": None, "token_type": "Unable to generate token"}


