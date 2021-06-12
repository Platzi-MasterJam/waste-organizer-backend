import uvicorn
from api.routes.api import router as api_router
# from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
# from core.events import create_start_app_handler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    application = FastAPI()# (title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router)
    return application


app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
