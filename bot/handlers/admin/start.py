from aiogram import Router
from aiogram import F
from aiogram import types as t
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from handlers.admin.questions.states import CreateQuestionForm
from keyboards.admin import start_keyboard
from text import admin as txt

router = Router()


@router.message(CreateQuestionForm.question, F.text == 'Назад')
@router.message(CreateQuestionForm.answer, F.text == 'Назад')
@router.message(Command('start'))
async def start_handler(message: t.Message, state: FSMContext):
    await state.clear()
    keyboard = await start_keyboard()
    await message.answer(txt.START, reply_markup=keyboard)
