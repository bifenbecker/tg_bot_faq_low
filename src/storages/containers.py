from dependency_injector import containers, providers

from .db.orm import create_async_session


class Storages(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_session = providers.Resource(
        create_async_session,
        url=config.db.URL,
        echo=config.db.ECHO,
        pool_size=config.db.POOL_SIZE,
        max_overflow=config.db.MAX_OVERFLOW
    )

    # redis = providers.Factory()
