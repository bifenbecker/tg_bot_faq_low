from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    HOST: str
    NAME: str
    USER: str
    PASSWORD: str
    PORT: int
    ECHO: bool = False
    POOL_SIZE: int = 100
    MAX_OVERFLOW: int = 0
    EXPIRE_ON_COMMIT: bool = False

    @computed_field
    @property
    def URL(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    model_config = SettingsConfigDict(env_prefix="DB__", case_sensitive=False)
