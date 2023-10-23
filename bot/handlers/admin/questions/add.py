from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext

from handlers.admin.questions.states import CreateQuestionForm
from handlers.funcs.questions import create_question
from keyboards.admin import back_to_start_keyboard, start_keyboard
from models.db import session_factory
from text import admin as txt

router = Router()


@router.message(F.text == "Добавить вопрос")
async def start_create_question_handler(message: t.Message, state: FSMContext):
    if message.text:
        await state.set_state(CreateQuestionForm.question)
        keyboard = back_to_start_keyboard()
        await message.answer(text=txt.CREATE_QUESTION, reply_markup=keyboard)
    else:
        await message.answer(txt.ERROR_INPUT)


@router.message(CreateQuestionForm.question)
async def process_question_handler(message: t.Message, state: FSMContext):
    if message.text:
        await state.update_data(question=message.text)
        await state.set_state(CreateQuestionForm.answer)
        await message.answer(txt.CREATE_ANSWER)
    else:
        await message.answer(txt.ERROR_INPUT)


@router.message(CreateQuestionForm.answer)
async def process_answer_handler(message: t.Message, state: FSMContext):
    if message.text:
        await state.update_data(answer=message.text)
        data = await state.get_data()
        await state.clear()
        await create_question(session_factory, data)
        keyboard = await start_keyboard()
        await message.answer(txt.SUCCESS_CREATE_QUESTION, reply_markup=keyboard)
    else:
        await message.answer(txt.ERROR_INPUT)
