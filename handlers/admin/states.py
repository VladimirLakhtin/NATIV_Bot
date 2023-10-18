from aiogram.fsm.state import StatesGroup, State


class CreateQuestionForm(StatesGroup):
    question = State()
    answer = State()
