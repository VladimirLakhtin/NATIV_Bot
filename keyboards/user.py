from aiogram import types as t
from aiogram.utils.keyboard import InlineKeyboardBuilder

from models import Question


def questions_keyboard(questions: list[Question]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for q in questions:
        builder.button(text=q.question, callback_data=f"q_{q.id}")
    return builder
