from pathlib import Path

from pydantic import BaseSettings

source = Path(__file__).parent.parent.parent.parent.resolve()


class BaseConfig(BaseSettings):
    APP_NAME: str
    MODE: str

    class Config:
        env_file = f"{source}/.env"
