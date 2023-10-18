from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from callback_factories.user import QuestionAction, UserQuestionAction
from models import Question


def start_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список популярных вопросов")
    return builder


def questions_keyboard(questions: list[Question]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for q in questions:
        builder.button(text=q.question, callback_data=UserQuestionAction(
            action=QuestionAction.details,
            question_id=q.id,
        ))
    return builder


def question_info_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="К списку вопросов", callback_data=UserQuestionAction(
            action=QuestionAction.list_,
        ))
    return builder
