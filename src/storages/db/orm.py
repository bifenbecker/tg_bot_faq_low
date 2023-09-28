from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from loguru import logger

Base = declarative_base()


def create_async_session(url: str, echo: bool, pool_size: int,
                         max_overflow: int) -> async_sessionmaker:
    logger.info(f"Connection to database - {url}")
    async_engine = create_async_engine(
        url,
        echo=echo,
        pool_size=pool_size,
        max_overflow=max_overflow,
    )
    return async_sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )
