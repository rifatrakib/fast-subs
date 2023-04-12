from .base import BaseConfig


class StagingConfig(BaseConfig):
    DEBUG: bool = False
    MODE: str = "Staging"
