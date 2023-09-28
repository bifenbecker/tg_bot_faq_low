from aiogram import Router

from src.bot import DirectorContainer

router = Router()
dispatcher = DirectorContainer.dispatcher()
dispatcher.include_router(router)
