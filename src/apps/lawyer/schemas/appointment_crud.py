from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AppointmentEntity(BaseModel):
    name: str
    phone: str
    question: str
    time: str


class AppointmentOrm(AppointmentEntity):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AppointmentCreate(AppointmentEntity):
    pass
