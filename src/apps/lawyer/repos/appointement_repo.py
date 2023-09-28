from .i_appointment_repo import IAppointmentRepo
from ..models import AppointmentModel
from ..schemas import AppointmentCreate


class AppointmentRepo(IAppointmentRepo):

    async def create(self, data: AppointmentCreate) -> AppointmentModel:
        async with self._db_session() as session:
            appointment = self.table(**data.model_dump())
            session.add(appointment)
            await session.commit()

        return appointment
