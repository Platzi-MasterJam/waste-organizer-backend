from fastapi import APIRouter

from api.routes import classifier

router = APIRouter()
# router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(classifier.router)