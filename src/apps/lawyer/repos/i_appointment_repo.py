from abc import ABC
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..models import AppointmentModel
from ..schemas import AppointmentCreate


class IAppointmentRepo(ABC):
    table = AppointmentModel

    def __init__(self, db_session: async_sessionmaker):
        self._db_session = db_session

    async def create(self, data: AppointmentCreate) -> AppointmentModel:
        raise NotImplementedError()
