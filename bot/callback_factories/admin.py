from enum import Enum

from aiogram.filters.callback_data import CallbackData


class QuestionAction(str, Enum):
    list_ = "list"
    details = "details"
    update = "update"
    delete = "delete"
    confirm_delete = "confirm_delete"


class AdminQuestionAction(CallbackData, prefix='adm'):
    action: QuestionAction
    question_id: int | None = None
    field: str | None = None
