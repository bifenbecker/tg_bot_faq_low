"""Database module."""

from typing import Union

from loguru import logger
from pydantic_core import MultiHostUrl
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from ..base_storage import BaseStorage


class Database(BaseStorage):
    def __init__(self, db_url: Union[MultiHostUrl, str], *args, **kwargs) -> None:
        super().__init__()
        url_connection = db_url if type(db_url) is str else db_url.unicode_string()
        self.log(url_connection)
        self.engine = create_async_engine(url_connection, pool_size=15, max_overflow=20)
        # self.engine = create_async_engine(url_connection, poolclass=NullPool)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    def log(self, info):
        logger.info(f"Database - {info}")
