from fastapi import APIRouter, Depends, HTTPException
from app.schemas.permission_schema import PermissionUpdate
from app.db.mongo import permission_collection
from app.utils.dependencies import admin_required
# from app.utils.permissions import require_permission
# from ..utils.permissions import require_permission
from ...utils.permissions import permission_dependency
from bson import ObjectId



router = APIRouter()

@router.post("/permissions")
async def update_permissions(data: PermissionUpdate, _: dict = Depends(permission_dependency("update_permissions"))):
    existing = await permission_collection.find_one({"user_id": data.user_id})

    # Safely get existing permissions, or use empty dict if not found
    current_permissions = existing.get("permissions", {}) if existing else {}
    merged_permissions = {**current_permissions, **data.permissions}

    await permission_collection.find_one_and_update(
        {"user_id": data.user_id},
        {"$set": {"permissions": merged_permissions}},
        upsert=True  # optionally True, in case you want to create if not exist
    )

    return {"status": "Permissions updated"}

@router.get("/permissions/{user_id}")
async def get_permissions(user_id: str, _: dict = Depends(permission_dependency("view_permissions"))):
    print(user_id)
    perms = await permission_collection.find_one({"user_id": user_id})
    if not perms:
        raise HTTPException(status_code=404, detail="No permissions found")
    return perms.get("permissions", {})


