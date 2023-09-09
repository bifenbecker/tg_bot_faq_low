from aiogram import Bot, Dispatcher


class Director:
    def __init__(
        self,
        dispatcher: Dispatcher,
        *bots: Bot,
    ):
        self.__bots = bots
        self.__dispatcher = dispatcher

    async def start(self, *args, **kwargs):
        await self.__dispatcher.start_polling(*self.__bots, *args, **kwargs)
