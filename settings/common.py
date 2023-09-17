from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .bot import BotSettings
from .project import ProjectSettings
from .storages import StorageSettings
from .dir import DirSettings
from .locale import LocaleSettings


class Settings(BaseSettings):
    storages: StorageSettings = Field(validation_alias="ST")
    bot: BotSettings = Field(validation_alias="BOT")
    project: ProjectSettings = Field(validation_alias="PROJECT")
    dir: DirSettings = Field(validation_alias="DIR")
    locale: LocaleSettings = Field(validation_alias="LOCALE")

    model_config = SettingsConfigDict(env_file="./config/env/.env", env_nested_delimiter="__", case_sensitive=False)
