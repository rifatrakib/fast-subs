from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from server.apps.demo.server.main import app as demo_app
from server.apps.gateway.server.main import app as gateway_app

app = FastAPI()

app.mount(f"/{gateway_app.openapi()['info']['title']}", gateway_app)
app.mount(f"/{demo_app.openapi()['info']['title']}", demo_app)


def merge_sub_app_metadata(sub_app: FastAPI, metadata: dict):
    sub_app_metadata = get_openapi(
        title=sub_app.title,
        version=sub_app.version,
        description=sub_app.description,
        routes=sub_app.routes,
    )

    api_base = sub_app_metadata["info"]["title"]
    for key, value in sub_app_metadata["paths"].items():
        metadata["paths"][f"/{api_base}{key}"] = value
        for method, method_value in value.items():
            metadata["paths"][f"/{api_base}{key}"][method]["operationId"] = f"{api_base}_{method_value['operationId']}"

    return metadata


def custom_openapi():
    metadata = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )

    sub_apps = [gateway_app, demo_app]
    for sub_app in sub_apps:
        metadata = merge_sub_app_metadata(sub_app, metadata)

    return metadata


app.openapi_schema = custom_openapi()


@app.get("/health")
async def health():
    return {"status": "ok"}
