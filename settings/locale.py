from typing import Optional

from pydantic_settings import BaseSettings


class LocaleSettings(BaseSettings):
    LANGS: Optional[str] = None
    DEFAULT: Optional[str] = None
    DOMAIN: Optional[str] = "messages"
