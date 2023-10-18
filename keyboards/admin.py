from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from models import Question


def start_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить вопрос")
    builder.button(text="Список вопросов")
    return builder


def back_to_start_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Назад")
    return builder


def questions_keyboard(questions: list[Question]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for q in questions:
        builder.button(text=q.question, callback_data=f"q_{q.id}")
    builder.adjust(1)
    return builder


def question_info_keyboard(q: Question) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="Изменить вопрос", callback_data=f'set_question_{q.id}')
    builder.button(text="Изменить ответ", callback_data=f'set_answer_{q.id}')
    builder.button(text="Удалить вопрос", callback_data=f'delete_question_{q.id}')
    builder.button(text="К списку вопросов", callback_data=f'questions_list')
    builder.adjust(2, 1, 1)
    return builder


def back_to_question_info_keyboard(question_id: int) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=f"q_{question_id}")
    return builder


def confirm_delete_question_keyboard(question_id: int) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="Да ✅", callback_data=f"confirm_delete_question_{question_id}")
    builder.button(text="Нет ❌", callback_data=f"q_{question_id}")
    return builder
