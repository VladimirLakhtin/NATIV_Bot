from aiogram.fsm.state import StatesGroup, State


class LessonSignUp(StatesGroup):
    type = State()
    send_contract = State()
    pay = State()
    send_questionnaire = State()


class ConsultSingUp(StatesGroup):
    send_form = State()
