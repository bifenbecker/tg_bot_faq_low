from aiogram import types, F
from ..router import router
from loguru import logger
from dependency_injector.wiring import inject, Provide
from ..container import ExampleContainer
from ..services import UserService


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_engine_from_config, async_sessionmaker
from sqlalchemy.pool import NullPool
from ..domain.entities.user import User
from settings import settings
import os

@router.message(F.text == "Hello")
async def message_handler_hello(message: types.Message):
    logger.info(message)
    await message.answer(message.text)


@router.message()
@inject
async def message_handler_echo(message: types.Message,
                               user_service: UserService = Provide[ExampleContainer.services.user_service]):
    # await user_service.create_user()
    logger.info("Start tests")
    # engine = create_async_engine(settings.storages.db.URL, echo=True, poolclass=NullPool)
    engine = create_async_engine(settings.storages.db.URL, echo=True, pool_size=10, max_overflow=20)
    AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    async with AsyncSessionLocal() as session:
        session.add(User(username="test pool_size 10"))
        await session.commit()
    await message.answer(message.text)
