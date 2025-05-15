from fastapi import Depends, HTTPException
from app.utils.dependencies import get_current_user
# from app.db.mongo import permission_collection
from app.db.models.permissions import PermissionsCollection


# Async function that checks permissions
async def require_permission(permission: str, user: dict = Depends(get_current_user)):
    if user.get("role") == "admin":
        return user  # Admin bypass
    user_perm = await PermissionsCollection.find_one({"user_id": user["sub"]})
    if user_perm:
        user_perm = user_perm.model_dump()
    else:
        user_perm = {}
    if not user_perm or not user_perm.get("permissions", {}).get(permission, False):
        raise HTTPException(status_code=403, detail=f"Permission '{permission}' required")
    return user

def permission_dependency(permission: str):
    async def dependency(user: dict = Depends(get_current_user)):
        return await require_permission(permission, user)
    return dependency