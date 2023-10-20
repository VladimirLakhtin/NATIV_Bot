from asyncio import run

from aiogram import F, Router
from aiogram import types as t
from aiogram.fsm.context import FSMContext

from handlers.funcs.admins import get_admins
from handlers.funcs.flags import check_consultation_available
from handlers.user.states import ConsultSingUp
from keyboards.user import send_form_confirm, start_keyboard
from models.db import session_factory
from text import user as txt
from text import admin as admin_txt

router = Router()


@router.message((F.text == "Записаться на консультацию ✏️") &
                (F.from_user.func(lambda user: not run(check_consultation_available(session_factory)))))
async def reject_sign_up_handler(message: t.Message):
    text = txt.CONSULTATION_NOT_AVAILABLE
    await message.answer(text)


@router.message((F.text == "Записаться на консультацию ✏️"))
async def start_sign_up_handler(message: t.Message, state: FSMContext):
    await state.set_state(ConsultSingUp.send_form)
    text = txt.CONSULTATION_AVAILABLE
    keyboard = send_form_confirm()
    await message.answer(text, reply_markup=keyboard)


@router.message(ConsultSingUp.send_form, F.text == "Отправлено 📩")
async def process_form_handler(message: t.Message, state: FSMContext):
    await state.clear()
    admins = await get_admins(session_factory)

    username = message.from_user.username
    keyboard = start_keyboard()
    if username:
        text = txt.FINISH_SIGN_UP
        admin_text = admin_txt.USER_SIGNED_UP_CONSULT.format(
            message.from_user.full_name, username)
        for admin in admins:
            await message.bot.send_message(chat_id=admin.tg_id, text=admin_text)
    else:
        admins_username = '\n'.join('@' + admin.username for admin in admins)
        text = txt.FINISH_SIGN_UP_WO_USERNAME.format(admins_username)

    await message.answer(text, reply_markup=keyboard)
