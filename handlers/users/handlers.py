from aiogram import Router
from aiogram import F
from aiogram import types as t
from aiogram.filters.command import Command

from ..funcs import get_questions
from keyboards.user import questions_keyboard
from models.db import session_factory

router = Router()


@router.message(Command("start"))
async def start_handler(message: t.Message):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)

    await message.answer("Hello", reply_markup=keyboard.as_markup())
