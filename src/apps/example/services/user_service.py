from ..domain.repositories import IUserRepo
from src.common import BaseService


class UserService(BaseService[IUserRepo]):
    async def create_user(self):
        return await self.repo.create_user()
