from pydantic import BaseModel
from typing import Dict

class PermissionUpdate(BaseModel):
    user_id: str
    permissions: Dict[str, bool]