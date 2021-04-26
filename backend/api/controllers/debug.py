from os import environ
from fastapi import APIRouter, Request

from core.utils import parse_dataset_csv

__all__ = ["router"]

router = APIRouter()


@router.get("/load_dataset/")
async def load_csv_dataset():
    await parse_dataset_csv()


@router.get("/")
async def debug_get(
    request: Request,
):
    return {
        "headers": request.headers,
        "envvars": dict(environ),
    }


@router.post("/")
async def debug_post():
    return {}
