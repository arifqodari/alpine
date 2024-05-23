from fastapi import FastAPI
from pydantic import BaseModel

from alpine.api.error_handler import register_error_handlers
from alpine.api.views import success_response
from alpine.util.logging import create_logger


class SearchQuery(BaseModel):
    query: str


app = FastAPI()
app = register_error_handlers(app)
logger = create_logger(__name__)


@app.get("/health")
def health():
    return success_response("OK")


@app.post("/search")
def search(query: SearchQuery):
    logger.info("this is search execution")
    return success_response(query.model_dump())
