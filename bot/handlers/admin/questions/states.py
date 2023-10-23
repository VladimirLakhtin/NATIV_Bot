from aiogram.fsm.state import StatesGroup, State


class CreateQuestionForm(StatesGroup):
    question = State()
    answer = State()


class UpdateQuestionForm(StatesGroup):
    question = State()
    answer = State()
