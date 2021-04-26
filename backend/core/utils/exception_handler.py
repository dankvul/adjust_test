from fastapi import exceptions as ex, responses
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import ValidationError
from starlette.requests import Request
from starlette import status

__all__ = ["exception_handlers"]


async def pydantic_exception_handler_func(request: Request, exc: ValidationError):
    resp = []
    for error in exc.errors():
        resp.append(
            {
                "field": error["loc"][-1],
                "message": error.get("msg"),
                "type": error.get("type"),
            }
        )
    return responses.UJSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=resp,
        headers={"Access-Control-Allow-Origin": "*"},
    )


async def http_exception_handler_func(request: Request, exception: HTTPException):
    return responses.UJSONResponse(
        content=[{"message": exception.detail}],
        status_code=getattr(exception, "status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
        headers={"Access-Control-Allow-Origin": "*"},
    )


exception_handlers = {
    RequestValidationError: pydantic_exception_handler_func,
    ex.HTTPException: http_exception_handler_func,
    status.HTTP_422_UNPROCESSABLE_ENTITY: pydantic_exception_handler_func,
    ValidationError: pydantic_exception_handler_func,
}
