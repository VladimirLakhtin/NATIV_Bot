from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext

from handlers.admin.questions.states import UpdateQuestionForm
from callback_factories.admin import AdminQuestionAction, QuestionAction
from handlers.funcs import update_question
from keyboards.admin import back_to_question_info_keyboard, question_info_keyboard
from models.db import session_factory
from text import admin as txt

router = Router()


@router.callback_query(AdminQuestionAction.filter(F.action == QuestionAction.update))
async def update_question_handler(callback: t.CallbackQuery, state: FSMContext,
                                  callback_data: AdminQuestionAction):
    await state.update_data(field=callback_data.field)
    next_state = getattr(UpdateQuestionForm, callback_data.field)
    await state.set_state(next_state)
    await state.update_data(question_id=callback_data.question_id)
    await state.update_data(main_msg=callback.message)

    keyboard = back_to_question_info_keyboard(callback_data.question_id)
    text = txt.UPDATE_QUESTION if callback_data.field == 'question' else txt.UPDATE_ANSWER
    await callback.message.edit_text(text=text)
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
    text = txt.QUESTION_TEMPLATE.format(question.question, question.answer)
    keyboard = question_info_keyboard(data['question_id'])
    await main_message.edit_text(text, parse_mode='html')
    await main_message.edit_reply_markup(reply_markup=keyboard.as_markup())
