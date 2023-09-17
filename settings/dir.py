from typing import Optional

from pydantic_settings import BaseSettings


class DirSettings(BaseSettings):
    SRC: Optional[str] = "src"
    LOCALES: Optional[str] = "src/locales"
    APPS: Optional[str] = "src/apps"
