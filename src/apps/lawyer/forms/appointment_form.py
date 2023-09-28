from aiogram.fsm.state import StatesGroup, State


class AppointmentForm(StatesGroup):
    NAME = State()
    PHONE = State()
    QUESTION = State()
    TIME = State()
