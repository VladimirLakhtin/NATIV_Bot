from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить вопрос")
    return builder


def back_to_start_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Назад")
    return builder
