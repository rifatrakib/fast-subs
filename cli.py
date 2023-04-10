import json
from pathlib import Path

from typer import Typer

app = Typer()


@app.command()
def create_app(name: str):
    with open("repository-tree.json") as reader:
        tree = json.loads(reader.read())

    root_path = f"server/apps/{name}"
    for module, submodules in tree.items():
        module_path = f"{root_path}/{module}"
        Path(module_path).mkdir(parents=True, exist_ok=True)
        Path(f"{module_path}/__init__.py").touch()

        for submodule, files in submodules.items():
            if submodule == "root":
                [Path(f"{module_path}/{file}.py").touch() for file in files]
            elif submodule == "assets":
                [Path(f"{module_path}/{file}").touch() for file in files]
            else:
                submodule_path = f"{module_path}/{submodule}"
                Path(submodule_path).mkdir(parents=True, exist_ok=True)
                [Path(f"{submodule_path}/{file}.py").touch() for file in files]


if __name__ == "__main__":
    app()
