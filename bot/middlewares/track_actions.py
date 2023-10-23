from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.types import User as AiogramUser
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import Action, User
from models import Message as MyMessage
from models.db import session_factory
from models.message import get_message_by_text
from models.user import get_user_by_tg_id


async def create_action(
        session_factory: async_sessionmaker,
        aiogram_user: AiogramUser,
        is_message: bool,
        text: str = None,
        question_id: int = None,
):
    async with session_factory() as session:
        message_id = None

        user = await get_user_by_tg_id(aiogram_user.id)
        if user is None:
            user = User(tg_id=aiogram_user.id, username=aiogram_user.username)
            session.add(user)
            await session.commit()

        if text is not None:
            message = await get_message_by_text(text)
            if message is None:
                message = MyMessage(text=text)
                session.add(message)
                await session.commit()
            message_id = message.id

        action = Action(user_id=user.id, is_message=is_message,
                        message_id=message_id, question_id=question_id)
        session.add(action)

        await session.commit()


class TrackChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        await create_action(session_factory, aiogram_user=event.from_user,
                            is_message=True, text=event.text)
        return await handler(event, data)


class TrackChatActionCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        question_id = event.data.split(':')[-1]
        if question_id.isdigit():
            await create_action(session_factory, aiogram_user=event.from_user,
                                is_message=False, question_id=int(question_id))
        return await handler(event, data)
