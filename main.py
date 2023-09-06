import asyncio
import sys
import uvloop
import os
from settings import settings
from dotenv import load_dotenv
from loguru import logger
from src.bot import DirectorContainer
from src.storages.db import Database
from src.apps.example.domain.entities.user import User

load_dotenv('config/env/.env')

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool


async def main():
    # That works
    # logger.info("Start tests")
    # # engine = create_async_engine(settings.storages.db.URL, echo=True, poolclass=NullPool)
    # logger.info(os.environ)
    # logger.info(settings.storages.db.URL)
    # engine = create_async_engine(settings.storages.db.URL, echo=True, pool_size=10, max_overflow=20)
    # AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    # async with AsyncSessionLocal() as session:
    #     session.add(User(username="test pool_size 10"))
    #     await session.commit()


    # That works
    # 2 vars works
    # engine = create_async_engine(settings.storages.db.URL, echo=True, poolclass=NullPool)
    # # engine = create_async_engine(settings.storages.db.URL, echo=True, pool_size=10, max_overflow=20)
    # AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    # async with AsyncSessionLocal() as session:
    #     async with session.begin():
    #         session.add(User(username="test no pull"))

    director = DirectorContainer.director()
    logger.info("Start polling")
    await director.start()


if __name__ == '__main__':
    if sys.version_info >= (3, 11):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    else:
        uvloop.install()
        asyncio.run(main())
