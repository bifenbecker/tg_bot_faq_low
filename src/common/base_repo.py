from abc import ABCMeta
from typing import TypeVar, Generic
from ..storages.db import Base as BaseModel

StorageType = TypeVar("StorageType")


class BaseRepo(Generic[StorageType], metaclass=ABCMeta):
    table: BaseModel

    def __init__(self, storage: StorageType):
        self._storage = storage

    @property
    def storage(self) -> StorageType:
        return self._storage
