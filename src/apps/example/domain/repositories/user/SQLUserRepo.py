from .IUserRepo import IUserRepo
from src.storages.db import Database


class SQLUserRepo(IUserRepo[Database]):

    async def create_user(self):
        async with self.storage.async_session() as session:
            user = self.table(username="telegram user")
            session.add(user)
            await session.commit()
        return user
