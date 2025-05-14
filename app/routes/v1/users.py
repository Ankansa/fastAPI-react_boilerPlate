from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schema import UserCreate, UserOut
# from app.db.mongo import user_collection
from app.db.models.users import UserCollection
from app.utils.auth import hash_password
from app.utils.dependencies import admin_required
from bson import ObjectId
# from app.utils.permissions import require_permission
# from ..utils.permissions import require_permission
from ...utils.permissions import permission_dependency
from bson import ObjectId



router = APIRouter()

@router.post("/users", response_model=UserOut)
async def create_user(user: UserCreate, current_user: dict = Depends(permission_dependency("create_user"))):
    if await UserCollection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    admin_details = await UserCollection.find_one({"_id": ObjectId(current_user["sub"])})
    user_data = user.dict()
    print(user_data)
    print(admin_details)
    organization_name = user_data.get("organization_name") if user_data.get("organization_name") else admin_details.get("organization_name")
    organization_country = user_data.get("organization_country") if user_data.get("organization_country") else admin_details.get("organization_country")
    user_data["name"] = user_data["name"].strip()
    user_data["email"] = user_data["email"].lower()
    user_data["password_hash"] = hash_password(user_data.pop("password"))
    user_data["role"] = user_data["role"].strip()
    user_data["added_by"] = current_user["sub"]
    user_data["organization_name"] = organization_name
    user_data["organization_country"] = organization_country
    user_data["created_at"] = user_data["updated_at"] = datetime.utcnow().isoformat()
    user_data["is_active"] = True
    user_data["custom_fields"] = user_data.get("custom_fields", {})
    result = await UserCollection.insert_one(user_data)
    return {**user_data, "id": str(result.inserted_id)}

@router.get("/users")
async def list_users(_: dict = Depends(permission_dependency("view_users"))):
    users = await UserCollection.find().to_list(length=100)
    return [
        {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "custom_fields": user.get("custom_fields", {}),
            "added_by": user.get("added_by","Self"),
            "organization_name": user.get("organization_name"),
            "organization_country": user.get("organization_country"),
            "created_at": user.get("created_at"),
            "updated_at": user.get("updated_at"),
        }
        for user in users
    ]