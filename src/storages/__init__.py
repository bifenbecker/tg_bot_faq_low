from .containers import Storages
from .base_storage import BaseStorage

storages = Storages()

__all__ = (
    storages,
    Storages,
    BaseStorage
)
