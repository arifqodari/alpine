from fastapi import Request
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from alpine.api.views import error_response


async def request_validation_handler(_: Request, error: RequestValidationError):
    validation_errors = [(".".join(str(x) for x in e["loc"]), e["type"]) for e in error.errors()]
    return error_response(error.__class__.__name__, 400, validation_errors)


async def http_exception_handler(_, error: StarletteHTTPException):
    return error_response(error.detail, error.status_code)


async def internal_error_handler(_, error: Exception):
    return error_response(error.__class__.__name__, 500)


def register_error_handlers(app: FastAPI) -> FastAPI:
    app.exception_handler(RequestValidationError)(request_validation_handler)
    app.exception_handler(StarletteHTTPException)(http_exception_handler)
    app.exception_handler(Exception)(internal_error_handler)
    return app
