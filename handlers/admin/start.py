from aiogram import Router
from aiogram import F
from aiogram import types as t

from keyboards.admin import start_keyboard
from models.db import session_factory

router = Router()


@router.message((F.text == "/start") & (F.from_user.username == "yummy_lvl"))
async def start_handler(message: t.Message):
    keyboard = start_keyboard()
    await message.answer("Hello, admin!",
                         reply_markup=keyboard.as_markup(resize_keyboard=True))
