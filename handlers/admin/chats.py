from aiogram import F, Router
from aiogram import types as t
from aiogram.types import FSInputFile

import config
from handlers.funcs.write_chats import write_chats


router = Router()


@router.message(F.text.startswith("Выгрузить данные"))
async def get_chats_handler(message: t.Message):
    await write_chats()
    logs = FSInputFile(str(config.CHATS_ZIP_PATH))
    await message.bot.send_document(chat_id=message.chat.id, document=logs)
