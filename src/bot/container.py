from dependency_injector import containers, providers
from aiogram import Bot, Dispatcher
from .director import Director


class DirectorContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    bot = providers.Singleton(Bot, token=config.TOKEN)

    dispatcher = providers.Singleton(
        Dispatcher
    )

    director = providers.Singleton(
        Director,
        dispatcher,
        bot
    )

