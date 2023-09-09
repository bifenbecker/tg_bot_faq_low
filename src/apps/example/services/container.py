from dependency_injector import containers, providers

from ..domain.repositories.user.SQLUserRepo import SQLUserRepo
from .user_service import UserService


class Services(containers.DeclarativeContainer):
    storages = providers.DependenciesContainer()

    repo = providers.Factory(SQLUserRepo, storage=storages.db)

    user_service = providers.Factory(UserService, repo=repo)
