from ..repos import IAppointmentRepo
from ..schemas import AppointmentCreate, AppointmentOrm


class AppointmentService:

    def __init__(self, repo: IAppointmentRepo):
        self.repo = repo

    async def create(self, data: AppointmentCreate) -> AppointmentOrm:
        appointment = await self.repo.create(data=data)
        return AppointmentOrm.model_validate(appointment)
