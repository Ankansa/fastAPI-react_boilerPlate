from fastapi import APIRouter, Depends, HTTPException
from ...utils.permissions import permission_dependency
from app.db.mongo import sells_collection
from typing import Optional, Dict, Any, List, AnyStr


router = APIRouter()

@router.get("/sales/{page}/{count}")
async def get_sales(pages: int, count: int, _: dict = Depends(permission_dependency("view_sales")))-> List[Dict[str,Any]]:
    """We are using data base pagination in this api
    - Page is the page index of pagination
    - Count is maximum data count in the page
    """
    if pages < 1 or count < 1:
        raise HTTPException(status_code=400, detail="Pages and count must be greater than 0")

    skip = (pages - 1) * count

    cursor = sells_collection.aggregate([
        {"$project": {"_id": 0}},
        {"$skip": skip},
        {"$limit": count}
    ])

    datas = await cursor.to_list(length=count)

    if not datas:
        raise HTTPException(status_code=404, detail="No data found")
    return datas