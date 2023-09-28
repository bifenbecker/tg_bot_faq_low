from .appointment_service import AppointmentService
from .container import Services

container = Services()

__all__ = (
    "Services",
    "AppointmentService"
)
