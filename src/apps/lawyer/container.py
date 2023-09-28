from dependency_injector import containers, providers

from src.storages import Storages

from .services import Services


class LawyerContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    storages = providers.Container(Storages)

    services = providers.Container(Services, storages=storages)
