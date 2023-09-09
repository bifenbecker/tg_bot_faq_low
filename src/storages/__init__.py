from .base_storage import BaseStorage
from .containers import Storages

storages = Storages()

__all__ = (storages, Storages, BaseStorage)
