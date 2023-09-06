from dependency_injector import containers, providers
from .db import Database


class Storages(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(
        Database,
        db_url=config.db.URL
    )

    # redis = providers.Factory()
