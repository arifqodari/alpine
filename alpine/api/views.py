import re

from typing import List, Optional
from fastapi.responses import JSONResponse




def _camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).upper()


def success_response(data):
    return JSONResponse(
        dict(
            data=data
        )
    )


def error_response(error: str, code: int = 500, descriptions: Optional[List] = None):
    if descriptions is None:
        descriptions = []

    return JSONResponse(
        dict(
            error=error,
            code=code,
            error_description=[
                {"field": desc[0], "message": desc[1]} for desc in descriptions
            ]
        ),
        status_code=code,
    )
