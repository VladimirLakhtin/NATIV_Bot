from asyncio import run

from aiogram import F, Router
from aiogram import types as t

from callback_factories.admin import AdminQuestionAction, QuestionAction
from handlers.funcs.questions import get_questions, get_question_by_id
from keyboards.admin import questions_keyboard, question_info_keyboard
from models.db import session_factory
from text import admin as txt

router = Router()


@router.message(F.text == "Популярные вопросы")
async def question_list_handler(message: t.Message):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = txt.QUESTIONS_LIST if questions else txt.EMPTY_QUESTIONS_LIST
    await message.answer(text, reply_markup=keyboard)


@router.callback_query(AdminQuestionAction.filter(F.action == QuestionAction.list_))
async def question_list_callback_handler(query: t.CallbackQuery):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = txt.QUESTIONS_LIST if questions else txt.EMPTY_QUESTIONS_LIST
    await query.message.edit_text(text)
    await query.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(AdminQuestionAction.filter(F.action == QuestionAction.details))
async def question_info_handler(query: t.CallbackQuery, callback_data: AdminQuestionAction):
    keyboard = question_info_keyboard(callback_data.question_id)
    question = await get_question_by_id(session_factory, callback_data.question_id)
    text = txt.QUESTION_TEMPLATE.format(question.question, question.answer)
    await query.message.edit_text(text, parse_mode='html')
    await query.message.edit_reply_markup(reply_markup=keyboard)
