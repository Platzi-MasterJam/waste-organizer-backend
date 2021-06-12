from models.user import UserResult, User
from typing import List

from fastapi import APIRouter
from typing import List
from core import db


router = APIRouter()

@router.post(
    "/users", name="create-user", response_model=User
)
async def create_product(item: User):
    instance = item.dict()
    db.db_users.put(instance)
    return item


@router.post(
    "/results", name="create-user-result", response_model=UserResult
)
async def create_result(item: UserResult):
    instance = item.dict()
    db.db_results.put(instance)
    return item


@router.get(
    "/results", name="list-user-result", response_model=List[UserResult]
)
async def list_result():
    items = list(*db.db_results.fetch())
    return items