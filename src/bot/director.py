from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware

from settings import settings


class Director:
    def __init__(
            self,
            dispatcher: Dispatcher,
            *bots: Bot,
    ):
        self.__bots = bots
        self.__dispatcher = dispatcher

    async def start(self, *args, **kwargs):
        self.__dispatcher.startup.register(self.startup)
        self.__dispatcher.shutdown.register(self.startup)
        await self.__dispatcher.start_polling(*self.__bots, *args, **kwargs)

    async def startup(self):
        i18n = I18n(path=settings.dir.LOCALES, default_locale=settings.locale.DEFAULT, domain=settings.locale.DOMAIN)
        self.__dispatcher.message.middleware(SimpleI18nMiddleware(i18n=i18n))
        await self.__bots[0].set_my_commands([
            BotCommand(command="/start", description="Start bot"),
        ])

    async def shutdown(self):
        pass
