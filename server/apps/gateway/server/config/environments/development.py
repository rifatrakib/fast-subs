from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    MODE: str = "Development"
