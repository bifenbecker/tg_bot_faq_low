from src.common import BaseService

from ..domain.entities import User
from ..domain.repositories import IUserRepo


class UserService(BaseService[IUserRepo]):
    async def create_user(self) -> User:
        user: User = await self.repo.create_user()
        return user
