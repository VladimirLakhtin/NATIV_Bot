from aiogram import Router, F
from aiogram import types as t
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from handlers.user.states import LessonSignUp, ConsultSingUp
from keyboards.user import start_keyboard
from text import user as txt

router = Router()


@router.message(LessonSignUp.type, F.text == "Назад 🔙")
@router.message(LessonSignUp.pay, F.text == "Назад 🔙")
@router.message(LessonSignUp.send_contract, F.text == "Назад 🔙")
@router.message(LessonSignUp.send_questionnaire, F.text == "Назад 🔙")
@router.message(ConsultSingUp.send_form, F.text == "Назад 🔙")
@router.message(Command("start"))
async def start_handler(message: t.Message, state: FSMContext):
    await state.clear()
    keyboard = start_keyboard()
    await message.answer(txt.START, reply_markup=keyboard)
