from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext

from handlers.admin.states import CreateQuestionForm
from keyboards.admin import back_to_start_keyboard
from models.db import session_factory

router = Router()


@router.message((F.from_user.username == "yummy_lvl") & (F.text == "Добавить вопрос"))
async def start_create_question_handler(message: t.Message, state: FSMContext):
    await state.set_state(CreateQuestionForm.question)
    keyboard = back_to_start_keyboard()
    await message.answer("Введите популярный вопрос:",
                         reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.message(CreateQuestionForm.question)
async def process_question_handler(message: t.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await state.set_state(CreateQuestionForm.answer)
    await message.answer("Введите ответ на этот вопрос:")


@router.message(CreateQuestionForm.question)
async def process_answer_handler(message: t.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await state.set_state(CreateQuestionForm.answer)
    await message.answer("Введите ответ на этот вопрос:")
