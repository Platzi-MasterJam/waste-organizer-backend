from models.products import ProductGuessing
from models.user import UserResult
from typing import List
from db.products import Product
from datetime import date
from fastapi import APIRouter, Response
from typing import List
from core import db


router = APIRouter()


@router.get(
    "/products", name="list-products", response_model=List[Product]
)
async def list_product():
    items = list(*db.db_products.fetch())
    return items

@router.post(
    "/products", name="create-products", response_model=Product
)
async def create_product(item: Product, response: Response):
    # TODO Change response status for 201
    instance = item.dict()
    response.status_code = 201
    db.db_products.put(instance)
    return item

@router.post(
    "products/evaluate", name="evaluate-products", response_model=UserResult
)
async def evaluate_products(username:str, product_guessings: List[ProductGuessing]):
    """
    Evaluate a list of products guessings and store the result of that evaluation.
    """
    products = list(*db.db_products.fetch())
    product_keys = [product["key"] for product in products]
    right_answers = 0
    bad_answers = 0
    date_result = str(date.today())
    for guessing in product_guessings:
        if guessing.key in product_keys:
            right_answers += 1
        else:
            bad_answers += 1

    result = UserResult(username=username, date=date_result, right_answers=right_answers, bad_answers=bad_answers)
    return result
