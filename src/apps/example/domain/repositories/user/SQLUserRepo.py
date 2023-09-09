from src.storages.db import Database

from src.apps.example.domain.entities import User
from .IUserRepo import IUserRepo


class SQLUserRepo(IUserRepo[Database]):
    async def create_user(self) -> User:
        async with self.storage.async_session() as session:
            user = self.table(username="telegram user")
            session.add(user)
            await session.commit()
        return user
