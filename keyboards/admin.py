from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from callback_factories.admin import QuestionAction, AdminQuestionAction
from handlers.funcs.flags import check_consultation_available
from models import Question
from models.db import session_factory


async def start_keyboard() -> ReplyKeyboardMarkup:
    cons = await check_consultation_available(session_factory)
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить вопрос")
    builder.button(text="Популярные вопросы")
    builder.button(text=f"Запись на консультацию {'🟢' if cons else '🔴'}")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)


def back_to_start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Назад")
    return builder.as_markup(resize_keyboard=True)


def questions_keyboard(questions: list[Question]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for q in questions:
        builder.button(text=q.question, callback_data=AdminQuestionAction(
            action=QuestionAction.details,
            question_id=q.id,
        ))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def question_info_keyboard(question_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Изменить вопрос", callback_data=AdminQuestionAction(
        action=QuestionAction.update,
        question_id=question_id,
        field="question",
    ))
    builder.button(text="Изменить ответ", callback_data=AdminQuestionAction(
        action=QuestionAction.update,
        question_id=question_id,
        field="answer",
    ))
    builder.button(text="Удалить вопрос", callback_data=AdminQuestionAction(
        action=QuestionAction.delete,
        question_id=question_id,
    ))
    builder.button(text="К списку вопросов", callback_data=AdminQuestionAction(
        action=QuestionAction.list_,
    ))
    builder.adjust(2, 1, 1)
    return builder.as_markup(resize_keyboard=True)


def back_to_question_info_keyboard(question_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=AdminQuestionAction(
        action=QuestionAction.details,
        question_id=question_id,
    ))
    return builder.as_markup(resize_keyboard=True)


def confirm_delete_question_keyboard(question_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Да ✅", callback_data=AdminQuestionAction(
        action=QuestionAction.confirm_delete,
        question_id=question_id,
    ))
    builder.button(text="Нет ❌", callback_data=AdminQuestionAction(
        action=QuestionAction.details,
        question_id=question_id,
    ))
    return builder.as_markup(resize_keyboard=True)
