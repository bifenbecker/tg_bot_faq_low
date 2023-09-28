from dependency_injector import providers, containers

from .appointment_service import AppointmentService
from ..repos import AppointmentRepo


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()
    storages = providers.DependenciesContainer()

    appointment_repo = providers.Singleton(
        AppointmentRepo,
        db_session=storages.db_session
    )

    appointment_service = providers.Singleton(
        AppointmentService,
        repo=appointment_repo
    )
