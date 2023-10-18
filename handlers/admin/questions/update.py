from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext

from handlers.admin.questions.states import UpdateQuestionForm
from handlers.funcs import update_question
from keyboards.admin import back_to_question_info_keyboard, question_info_keyboard
from models.db import session_factory

router = Router()


@router.callback_query(F.data.startswith('set_'))
async def update_question_handler(callback: t.CallbackQuery, state: FSMContext):
    _, field, question_id = callback.data.split('_')
    await state.update_data(field=field)
    next_state = getattr(UpdateQuestionForm, field)
    await state.set_state(next_state)
    await state.update_data(question_id=question_id)
    await state.update_data(main_msg=callback.message)

    keyboard = back_to_question_info_keyboard(question_id)
    rus_field = 'вопрос' if field == 'question' else 'ответ'
    await callback.message.edit_text(text=f"Введите новый {rus_field}:")
    await callback.message.edit_reply_markup(reply_markup=keyboard.as_markup())


@router.message(UpdateQuestionForm.answer)
@router.message(UpdateQuestionForm.question)
async def process_update_question(message: t.Message, state: FSMContext):
    data = await state.get_data()
    main_message = data['main_msg']
    await state.clear()

    update_data = {data['field']: message.text}
    question = await update_question(session_factory, data['question_id'], update_data)

    await message.delete()
    text = question.question + "\n" + question.answer
    keyboard = question_info_keyboard(question)
    await main_message.edit_text(text)
    await main_message.edit_reply_markup(reply_markup=keyboard.as_markup())
