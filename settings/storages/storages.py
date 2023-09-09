from pydantic_settings import BaseSettings

from .db import DatabaseSettings


class StorageSettings(BaseSettings):
    db: DatabaseSettings
