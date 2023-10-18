from aiogram import Router
from aiogram import F
from aiogram import types as t

from keyboards.admin import start_keyboard
from text import admin as txt

router = Router()


@router.message((F.text == "/start") & (F.from_user.username == "yummy.lvl"))
async def start_handler(message: t.Message):
    keyboard = start_keyboard()
    await message.answer(txt.START,
                         reply_markup=keyboard.as_markup(resize_keyboard=True))
