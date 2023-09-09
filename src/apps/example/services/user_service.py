from src.common import BaseService

from ..domain.repositories import IUserRepo
from ..domain.entities import User


class UserService(BaseService[IUserRepo]):
    async def create_user(self) -> User:
        user: User = await self.repo.create_user()
        return user
