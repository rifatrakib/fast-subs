import zipfile
from pathlib import Path
from typing import Union

import uvicorn
from typer import Typer

app = Typer()


@app.command()
def create_app(name: str):
    zip_path = "server/apps/template/app.zip"
    extract_path = f"server/apps/{name}"

    with zipfile.ZipFile(zip_path) as zip_file:
        zip_file.extractall(extract_path)

    env_path = f"{extract_path}/.env"
    with open(env_path, "w") as writer:
        writer.write(f"APP_NAME={name}\nMODE=development\n")


@app.command()
def rename_app(old_name: str, new_name: str):
    path = Path(f"server/apps/{old_name}")
    path.rename(f"server/apps/{new_name}")

    env_path = f"server/apps/{new_name}/.env"
    with open(env_path, "r") as reader:
        lines = reader.readlines()
        for idx, line in enumerate(lines):
            if line.startswith("APP_NAME="):
                break

    lines[idx] = f"APP_NAME={new_name}\n"
    with open(env_path, "w") as writer:
        writer.write("".join(lines))


@app.command()
def create_router(app: str, name: str):
    modules = [
        "database",
        "models",
        "routes",
        "schemas/database",
        "schemas/requests",
        "schemas/responses",
    ]

    for module in modules:
        router_path = f"server/apps/{app}/server/{module}/{name}.py"
        Path(router_path).touch()


@app.command()
def start_server(name: Union[str, None] = None):
    app_dir = f"server/apps/{name}" if name else "./"
    uvicorn.run(
        "server.main:app",
        host="0.0.0.0",
        port=8000,
        app_dir=app_dir,
        reload=True,
    )


if __name__ == "__main__":
    app()
