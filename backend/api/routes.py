from fastapi import APIRouter

from config import DEBUG

from api.controllers import debug, dataset

api_router = APIRouter()

api_router.include_router(dataset.router, prefix="/dataset", tags=["dataset"])

if DEBUG:
    api_router.include_router(debug.router, prefix="/debug", tags=["debug"])
