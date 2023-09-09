from enum import Enum

from pydantic_settings import BaseSettings


class EnvEnum(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


class ProjectSettings(BaseSettings):
    NAME: str
    VERSION: str
    ENV: EnvEnum = EnvEnum.DEV
