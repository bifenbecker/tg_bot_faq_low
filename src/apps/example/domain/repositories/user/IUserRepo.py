from abc import abstractmethod
from typing import Generic, TypeVar

from src.apps.example.domain.entities.user import User
from src.common import BaseRepo

T = TypeVar("T")


class IUserRepo(Generic[T], BaseRepo[T]):
    table = User

    @abstractmethod
    async def create_user(self) -> User:
        raise NotImplementedError
