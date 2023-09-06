from dependency_injector import containers, providers
from src.storages import Storages
from .services import Services


# {AppName}Container
class ExampleContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    storages = providers.Container(
        Storages,
        config=config.storages
    )

    services = providers.Container(
        Services,
        storages=storages
    )
