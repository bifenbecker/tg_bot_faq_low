from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from aiogram import F
from aiogram.fsm.context import FSMContext
from dependency_injector.wiring import inject, Provide
from loguru import logger

from ..router import router
from ..forms import AppointmentForm
from ..services import AppointmentService
from ..schemas import AppointmentCreate
from ..container import LawyerContainer


@router.message(CommandStart())
@inject
async def start_command_handler(message: Message) -> None:
    keyboard_builder = ReplyKeyboardBuilder(
        [
            [KeyboardButton(text=_("Наши услуги")), KeyboardButton(text=_("Запись на консультацию"))],
        ]
    )
    await message.answer(
        text=_(
            """Полный спектр юридических услуг бизнесу, гражданам, а также некоммерческим организациям
На рынке 36 лет!"""
        ),
        reply_markup=keyboard_builder.as_markup(resize_keyboard=True),
    )


@router.message(F.text == __("Наши услуги"))
async def our_services_handler(message: Message) -> None:
    await message.answer(
        text=_(
            """Авторская методика взыскания всех видов задолженности

Ликвидация бизнеса

Работа с ICO и IPO. Токены. Разработка смартконтрактов. Внесение криптовалюты в УФ

Все виды строительных споров

Легализация решений зарубежных судов

Обжалование итогов проведения процедур закупок

Разработка и экспертиза документов

Правовая поддержка международных перевозчиков и экспедиторов

Все виды претензионно–исковой работы

Абонентское обслуживание юрлиц и ИП

Лицензии, Аттестация, Сертификация
Регистрация товарного знака | знака обслуживания

Открытие бизнеса под ключ

Кадровое делопроизводство

Аудит

Полный спектр работ с коммерческой недвижимостью

Правовое сопровождение всего процесса строительства

Апостилизация, легализация документов в МИД, перевод, нотариальное заверение под ключ

Сопровождение сделок в корпоративном праве

Получение разрешений на размещение реклам/вывесок

Все виды в сфере трудовой миграции

Взыскание алиментов"""
        )
    )


@router.message(F.text == __("Запись на консультацию"))
async def appointment_for_consultation(message: Message, state: FSMContext) -> None:
    await state.set_state(state=AppointmentForm.NAME)
    await message.answer(text=_("Ваше имя"), reply_markup=ReplyKeyboardRemove())


@router.message(AppointmentForm.NAME)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(state=AppointmentForm.PHONE)
    await message.answer(
        text=_("Номер телефона"),
        reply_markup=ReplyKeyboardBuilder(
            [[KeyboardButton(text=_("Поделиться телефоном"), request_contact=True)]]
        ).as_markup(resize_keyboard=True),
    )


@router.message(AppointmentForm.PHONE)
async def process_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(state=AppointmentForm.QUESTION)
    await message.answer(text=_("Ваш вопрос"), reply_markup=ReplyKeyboardRemove())


@router.message(AppointmentForm.QUESTION)
async def process_question(message: Message, state: FSMContext) -> None:
    await state.update_data(question=message.text)
    await state.set_state(state=AppointmentForm.TIME)
    await message.answer(text=_("Укажите удобное для вас время"))


@router.message(AppointmentForm.TIME)
@inject
async def process_question(
        message: Message, state: FSMContext,
        appointment_service: AppointmentService = Provide[LawyerContainer.services.appointment_service]
) -> None:
    data = await state.update_data(time=message.text)
    try:
        await appointment_service.create(AppointmentCreate(**data))
    except Exception as e:
        logger.exception(e)
        await message.answer(text=_("Не удалось оставить заявку"))
    else:
        await message.answer(text=_("Ваша форма заполнена и сохранена!"))
    finally:
        await state.clear()
