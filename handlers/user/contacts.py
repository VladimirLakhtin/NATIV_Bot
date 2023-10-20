from aiogram import F, Router
from aiogram import types as t

import config
from text import user as txt

router = Router()


@router.message((F.text == "Где мы находимся? 📍"))
async def contacts_handler(message: t.Message):
    text = txt.CONTACTS
    await message.answer(text, parse_mode='html')
    await message.bot.send_location(chat_id=message.chat.id,
                                    latitude=config.LATITUDE,
                                    longitude=config.LONGITUDE)
