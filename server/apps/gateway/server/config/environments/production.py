from .base import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG: bool = False
    MODE: str = "Production"
