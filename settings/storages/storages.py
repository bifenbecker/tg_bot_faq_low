from pydantic_settings import BaseSettings, SettingsConfigDict
from .db import DatabaseSettings
from .redis import RedisSettings


class StorageSettings(BaseSettings):
    db: DatabaseSettings
    # redis: RedisSettings

