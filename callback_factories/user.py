from enum import Enum

from aiogram.filters.callback_data import CallbackData


class QuestionAction(str, Enum):
    list_ = "list"
    details = "details"


class UserQuestionAction(CallbackData, prefix='user'):
    action: QuestionAction
    question_id: int | None = None
