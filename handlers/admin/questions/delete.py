from aiogram import F, Router
from aiogram import types as t

from handlers.funcs import delete_question, get_question_by_id, get_questions
from keyboards.admin import confirm_delete_question_keyboard, questions_keyboard
from models.db import session_factory

router = Router()


@router.callback_query(F.data.startswith('delete_question_'))
async def delete_question_handler(callback: t.CallbackQuery):
    question_id = int(callback.data.split('_')[-1])
    keyboard = confirm_delete_question_keyboard(question_id)
    await callback.message.edit_text(text="Вы уверены, что хотите удалить этот вопрос?")
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())


@router.callback_query(F.data.startswith('confirm_delete_question_'))
async def delete_question_handler(callback: t.CallbackQuery):
    question_id = int(callback.data.split('_')[-1])
    await delete_question(session_factory, question_id)

    questions = await get_questions(session_factory)
    keyboard = questions_keyboard(questions)
    text = "Популярные вопросы:" if questions else "Список популярных вопросов пуст"
    await callback.message.edit_text(text=text)
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())
