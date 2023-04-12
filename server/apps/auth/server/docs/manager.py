import os
from functools import lru_cache

from ..config.factory import settings
from ..services.validators import Tags


@lru_cache
def get_root_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    root = current_dir.replace(f"{cwd}\\", "")
    return root


def retrieve_api_metadata():
    with open(f"{get_root_dir()}/README.md") as reader:
        description = reader.read()

    api_metadata = {
        "title": settings.APP_NAME,
        "description": description,
        "version": "0.0.1",
        "terms_of_service": "https://fastapi.tiangolo.com/",
        "contact": {
            "name": f"Maintainer: {settings.APP_NAME}",
            "url": "https://fastapi.tiangolo.com/",
            "email": "example@mail.com",
        },
    }

    if settings.MODE != "production":
        api_metadata["openapi_url"] = "/openapi.json"
        api_metadata["docs_url"] = "/docs"
        api_metadata["redoc_url"] = "/redoc"
    else:  # pragma: no cover
        api_metadata["openapi_url"] = None
        api_metadata["docs_url"] = None
        api_metadata["redoc_url"] = None

    return api_metadata


def retrieve_tags_metadata():
    tags_metadata = [
        {
            "name": Tags.server_health.value,
            "description": "Verify *server operability* and *configuration variables*.",
            "externalDocs": {
                "description": "Server Health Check",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
    return tags_metadata
