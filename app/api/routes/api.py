from fastapi import APIRouter

from api.routes import products, users

router = APIRouter()
router.include_router(users.router)
router.include_router(products.router)