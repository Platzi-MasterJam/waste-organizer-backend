from typing import List
from db.products import Product

from fastapi import APIRouter
from typing import List
from core import db


router = APIRouter()


items = [
    {"name": "Lata", "type": "inorganic", "image": ""},
    {"name": "Manzana", "type": "organic", "image": ""},
]


@router.get(
    "/products", name="list-products", response_model=List[Product]
)
async def list_product():
    items = list(*db.db_products.fetch())
    return items

@router.post(
    "/products", name="create-products", response_model=Product
)
async def create_product(item: Product):
    instance = item.dict()
    db.db_products.put(instance)
    return item
