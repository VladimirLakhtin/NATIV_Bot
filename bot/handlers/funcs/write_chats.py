from io import StringIO
from itertools import groupby
from zipfile import ZipFile

import config
from models.action import get_actions
from text import admin as txt


async def write_chats() -> None:
    actions = await get_actions()

    with ZipFile(config.CHATS_ZIP_PATH, 'w') as zip_object:
        for user, user_actions in groupby(actions, key=lambda x: x.user):
            user_actions_s = "".join(
                txt.FILE_RECORD_TEMPLATE.format(
                    date=act.date,
                    user=act.user.username or act.user.tg_id,
                    text=act.message.text if act.is_message else act.question.question,
                )
                for act in user_actions
            )
            user_actions_sio = StringIO(user_actions_s)
            zip_object.writestr(f'user_{user.tg_id}.txt',
                                user_actions_sio.getvalue())