from aiogram import Router
from aiogram import types as t
from aiogram.filters.command import Command

from keyboards.user import start_keyboard
from text import user as txt

router = Router()


@router.message(Command("start"))
async def start_handler(message: t.Message):
    keyboard = start_keyboard()

    await message.answer(txt.START,
                         reply_markup=keyboard.as_markup(resize_keyboard=True))
