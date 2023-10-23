from aiogram import F, Router
from aiogram import types as t

from callback_factories.admin import AdminQuestionAction, QuestionAction
from handlers.funcs.questions import delete_question, get_questions
from keyboards.admin import confirm_delete_question_keyboard, questions_keyboard
from models.db import session_factory
from text import admin as txt

router = Router()


@router.callback_query(AdminQuestionAction.filter(F.action == QuestionAction.delete))
async def delete_question_handler(callback: t.CallbackQuery, callback_data: AdminQuestionAction):
    keyboard = confirm_delete_question_keyboard(callback_data.question_id)
    await callback.message.edit_text(text=txt.CONFIRM_DELETE_QUESTION)
    await callback.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(AdminQuestionAction.filter(F.action == QuestionAction.confirm_delete))
async def delete_question_handler(query: t.CallbackQuery, callback_data: AdminQuestionAction):
    await delete_question(session_factory, callback_data.question_id)
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = txt.QUESTIONS_LIST if questions else txt.EMPTY_QUESTIONS_LIST
    await query.message.edit_text(text=text)
    await query.message.edit_reply_markup(reply_markup=keyboard)
