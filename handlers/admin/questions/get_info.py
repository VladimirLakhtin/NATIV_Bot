from aiogram import F, Router
from aiogram import types as t

from handlers.funcs import get_questions, get_question_by_id
from keyboards.admin import questions_keyboard, question_info_keyboard
from models.db import session_factory

router = Router()


@router.message((F.from_user.username == "yummy_lvl") & (F.text == "Список вопросов"))
async def question_list_handler(message: t.Message):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = "Популярные вопросы:" if questions else "Список популярных вопросов пуст"
    await message.answer(text, reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "questions_list")
async def question_list_callback_handler(callback: t.CallbackQuery):
    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = "Популярные вопросы:" if questions else "Список популярных вопросов пуст"
    await callback.message.edit_text(text)
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())


@router.callback_query(F.data.startswith('q_'))
async def question_info_handler(callback: t.CallbackQuery):
    question_id = callback.data.split('_')[-1]
    question = await get_question_by_id(session_factory, int(question_id))
    keyboard = question_info_keyboard(question)
    text = question.question + "\n" + question.answer
    await callback.message.edit_text(text)
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())
