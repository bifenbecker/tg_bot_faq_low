from settings import settings
from .containers import Storages

Storages.config.from_dict(settings.storages.model_dump())
storages = Storages()

__all__ = (storages, Storages)
