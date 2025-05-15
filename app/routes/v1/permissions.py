from fastapi import APIRouter, Depends, HTTPException
from app.schemas.permission_schema import PermissionUpdate
# from app.db.mongo import permission_collection
from app.db.models.permissions import PermissionsCollection

from app.utils.dependencies import admin_required
# from app.utils.permissions import require_permission
# from ..utils.permissions import require_permission
from ...utils.permissions import permission_dependency
from bson import ObjectId



router = APIRouter()

@router.post("/permissions")
async def update_permissions(data: PermissionUpdate, _: dict = Depends(permission_dependency("update_permissions"))):
    existing = await PermissionsCollection.find_one(PermissionsCollection.user_id == data.user_id)

    current_permissions = existing.permissions if existing else {}
    merged_permissions = {**current_permissions, **data.permissions}

    if existing:
        existing.permissions = merged_permissions
        await existing.save()
    else:
        new_perm = PermissionsCollection(user_id=data.user_id, permissions=merged_permissions)
        await new_perm.insert()

    return {"status": "Permissions updated"}

@router.get("/permissions/{user_id}")
async def get_permissions(user_id: str, _: dict = Depends(permission_dependency("view_permissions"))):
    perms = await PermissionsCollection.find_one({"user_id": user_id})
    
    if not perms:
        raise HTTPException(status_code=404, detail="No permissions found")
    
    return perms.permissions  # assuming permissions is a Dict field in your model
