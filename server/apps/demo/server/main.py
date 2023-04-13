from fastapi import FastAPI

from .config.factory import settings
from .docs.manager import retrieve_api_metadata, retrieve_tags_metadata

app = FastAPI(**retrieve_api_metadata(), openapi_tags=retrieve_tags_metadata())


def customize_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        route.operation_id = f"{app.title}_{route.name}"


customize_operation_ids(app)


@app.get("/health")
async def health_check():
    return settings
