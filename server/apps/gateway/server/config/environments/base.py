from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings


@lru_cache
def get_source() -> str:
    source = Path(__file__).parent.parent.parent.parent.resolve()
    return f"{source}/.env"


class BaseConfig(BaseSettings):
    APP_NAME: str
    MODE: str

    class Config:
        env_file = get_source()
