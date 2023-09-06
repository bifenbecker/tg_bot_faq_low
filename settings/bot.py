from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class BotSettings(BaseSettings):
    TOKEN: str

    class Config:
        env_prefix = "BOT__"

    # model_config = SettingsConfigDict(env_prefix="BOT__", case_sensitive=False)
