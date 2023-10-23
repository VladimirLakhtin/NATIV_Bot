from aiogram import F, Router
from aiogram import types as t

from handlers.funcs.flags import change_lesson_available
from keyboards.admin import start_keyboard
from models.db import session_factory
from text import admin as txt

router = Router()


@router.message(F.text.startswith("Запись на занятие"))
async def change_available_handler(message: t.Message):
    is_available = await change_lesson_available(session_factory)
    keyboard = await start_keyboard()
    text = txt.LESSON_ON if is_available else txt.LESSON_OFF
    await message.answer(text=text, reply_markup=keyboard)
