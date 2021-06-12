from typing import List
from db.items import Item

from fastapi import APIRouter, HTTPException
from loguru import logger
from typing import List

from fastapi import Depends, FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware 
from starlette.responses import RedirectResponse



router = APIRouter()


items = [
    {"name": "Lata", "type": "inorganic", "image": ""},
    {"name": "Manzana", "type": "organic", "image": ""},
]


@router.get(
    "/items", name="items", response_model=List[Item]
)
async def list_items():
    
    return items

@router.post(
    "/items", name="items", response_model=Item
)
async def create_item(item: Item):
    breakpoint()
    return item