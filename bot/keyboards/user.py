from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from callback_factories.user import QuestionAction, UserQuestionAction
from models import Question


def start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Задать вопрос ❓")
    builder.button(text="Записаться на занятие 📝")
    builder.button(text="Записаться на консультацию ✏️")
    builder.button(text="Где мы находимся? 📍")
    builder.button(text="Связаться с нами ❤️")
    builder.adjust(1, 2, 2)
    return builder.as_markup(resize_keyboard=True)


def questions_keyboard(questions: list[Question]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for q in questions:
        builder.button(text=q.question, callback_data=UserQuestionAction(
            action=QuestionAction.details,
            question_id=q.id,
        ))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def question_info_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="К списку вопросов", callback_data=UserQuestionAction(
            action=QuestionAction.list_,
        ))
    return builder.as_markup(resize_keyboard=True)


def select_lesson_type() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Регулярные ⏰")
    builder.button(text="Интенсивы 🔥")
    builder.button(text="Назад 🔙")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def send_docs_confirm() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Отправлено 📩")
    builder.button(text="Назад 🔙")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def payment_confirm() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Оплачено 👌🏻")
    builder.button(text="Назад 🔙")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def send_form_confirm() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Отправлено 📩")
    builder.button(text="Назад 🔙")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

