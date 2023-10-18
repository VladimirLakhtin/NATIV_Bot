from aiogram import F, Router
from aiogram import types as t

from callback_factories.user import QuestionAction, UserQuestionAction
from handlers.funcs import get_questions, get_question_by_id
from keyboards.user import questions_keyboard, question_info_keyboard
from models.db import session_factory
from text import user as txt

router = Router()


@router.message((F.text == "Список популярных вопросов"))
async def question_list_handler(message: t.Message):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = txt.QUESTIONS_LIST if questions else txt.EMPTY_QUESTIONS_LIST
    await message.answer(text, reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(UserQuestionAction.filter(F.action == QuestionAction.list_))
async def question_list_callback_handler(query: t.CallbackQuery):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = txt.QUESTIONS_LIST if questions else txt.EMPTY_QUESTIONS_LIST
    await query.message.edit_text(text)
    await query.message.edit_reply_markup(reply_markup=keyboard.as_markup())


@router.callback_query(UserQuestionAction.filter(F.action == QuestionAction.details))
async def question_info_handler(query: t.CallbackQuery, callback_data: UserQuestionAction):
    question = await get_question_by_id(session_factory, callback_data.question_id)
    text = txt.QUESTION_TEMPLATE.format(question.question, question.answer)
    keyboard = question_info_keyboard()
    await query.message.edit_text(text, parse_mode='html')
    await query.message.edit_reply_markup(reply_markup=keyboard.as_markup())
