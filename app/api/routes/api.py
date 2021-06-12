from fastapi import APIRouter

from api.routes import products

router = APIRouter()
# router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(products.router)