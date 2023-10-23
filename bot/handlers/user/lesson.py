from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaDocument

import config
from handlers.funcs.admins import get_admins
from handlers.funcs.flags import check_lesson_available
from handlers.user.states import LessonSignUp
from keyboards.user import select_lesson_type, payment_confirm, send_docs_confirm, start_keyboard
from models.db import session_factory
from text import user as txt
from text import admin as admin_txt

router = Router()


@router.message(F.text == "Записаться на занятие 📝")
async def start_sign_up_handler(message: t.Message, state: FSMContext):
    if await check_lesson_available(session_factory):
        await state.set_state(LessonSignUp.type)
        keyboard = select_lesson_type()
        text = txt.SELECT_LESSON_TYPE
        await message.answer(text=text, reply_markup=keyboard)
    else:
        text = txt.LESSON_NOT_AVAILABLE
        await message.answer(text=text)


@router.message(LessonSignUp.type, F.text.in_(("Регулярные ⏰", "Интенсивы 🔥")))
async def sign_up_regular(message: t.Message, state: FSMContext):
    doc_type = 'regular' if message.text == "Регулярные ⏰" else 'intensive'
    await state.update_data(type=doc_type)
    await state.set_state(LessonSignUp.send_contract)
    contract_file = InputMediaDocument(
        media=FSInputFile(path=config.DOCUMENTS_DIR / f"{doc_type}_contract.pdf",
                          filename="Договор.pdf"),
    )
    rules_file = InputMediaDocument(
        media=FSInputFile(path=config.DOCUMENTS_DIR / f"{doc_type}_rules.pdf",
                          filename="Правила.pdf"),
    )
    text = txt.SEND_CONTRACT.format(config.EMAIL)
    keyboard = send_docs_confirm()
    await message.answer(text=text, reply_markup=keyboard, parse_mode='html')
    await message.bot.send_media_group(chat_id=message.chat.id,
                                       media=[contract_file, rules_file])


@router.message(LessonSignUp.send_contract, F.text == "Отправлено 📩")
async def process_contract(message: t.Message, state: FSMContext):
    await state.set_state(LessonSignUp.pay)
    text = txt.PAYMENT.format(config.EMAIL)
    keyboard = payment_confirm()
    await message.answer(text=text, reply_markup=keyboard, parse_mode='html')


@router.message(LessonSignUp.pay, F.text == "Оплачено 👌🏻")
async def process_payment(message: t.Message, state: FSMContext):
    await state.set_state(LessonSignUp.send_questionnaire)
    questionnaire_file = FSInputFile(path=config.DOCUMENTS_DIR / f"questionnaire.pdf",
                          filename="Анкета.pdf")
    text = txt.SEND_QUESTIONNARE.format(config.EMAIL)
    keyboard = send_docs_confirm()
    await message.bot.send_document(caption=text, reply_markup=keyboard, parse_mode="html",
                                    chat_id=message.chat.id, document=questionnaire_file)


@router.message(LessonSignUp.send_questionnaire, F.text == "Отправлено 📩")
async def process_send_docs(message: t.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    admins = await get_admins(session_factory)

    rus_type = 'регулярное' if data.get('type') == 'regular' else 'интенсив'
    username = message.from_user.username
    keyboard = start_keyboard()
    if username:
        text = txt.FINISH_SIGN_UP
        admin_text = admin_txt.USER_SIGNED_UP.format(
            message.from_user.full_name, rus_type, username)
        for admin in admins:
            if admin.tg_id:
                await message.bot.send_message(chat_id=admin.tg_id, text=admin_text)
    else:
        admins_username = '\n'.join('@' + admin.username for admin in admins)
        text = txt.FINISH_SIGN_UP_WO_USERNAME.format(admins_username)

    await message.answer(text, reply_markup=keyboard)
