from aiogram import F, Router
from aiogram import types as t

from handlers.funcs.admins import get_admins
from models.db import session_factory
from text import user as txt
from text import admin as admin_txt

router = Router()


@router.callback_query(F.data == "link:with:manager")
@router.message((F.text == "Связаться с нами ❤️"))
async def contacts_handler(message: t.Message):
    message = message.message if isinstance(message, t.CallbackQuery) else message
    admins = await get_admins(session_factory)
    username = message.from_user.username

    if username:
        text = txt.LINK_WITH_MANAGER
        admin_text = admin_txt.USER_CONNECT.format(
            message.from_user.full_name, username)
        for admin in admins:
            if admin.tg_id:
                await message.bot.send_message(chat_id=admin.tg_id, text=admin_text)
    else:
        admins_username = '\n'.join('@' + admin.username for admin in admins)
        text = txt.MANAGER_CONTACTS.format(admins_username)
    await message.answer(text, parse_mode='html')
