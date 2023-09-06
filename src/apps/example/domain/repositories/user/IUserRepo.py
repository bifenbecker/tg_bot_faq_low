from abc import abstractmethod
from typing import Generic, TypeVar
from src.common import BaseRepo
from src.apps.example.domain.entities.user import User

T = TypeVar("T")


class IUserRepo(Generic[T], BaseRepo[T]):
    table = User

    @abstractmethod
    async def create_user(self):
        raise NotImplementedError
