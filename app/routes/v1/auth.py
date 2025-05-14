from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from app.db.mongo import user_collection
from app.db.models.users import UserCollection
from app.utils.auth import verify_password, create_access_token, hash_password
from app.schemas.auth_schema import UserRegister, UserRegisterResoponse
from typing import Dict
router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str,str]:
    user = await UserCollection.find_one({"email": form_data.username})

    if user:
        user = user.model_dump()

    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(user["id"]), "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", response_model=UserRegisterResoponse)
async def register(user: UserRegister):

    if await UserCollection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered.")
    user_data = {
        "name": user.name,
        "email": user.email,
        "password_hash": hash_password(user.password),
        "role": "admin",
        "organization_name": user.organization_name,
        "organization_country": user.organization_country,
        "custom_fields": {},
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }
    result = await UserCollection.insert_one(user_data)
    return {
        "message": "Admin user created",
        "user_id": str(result.inserted_id),
        "email": user.email
    }