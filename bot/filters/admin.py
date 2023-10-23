from aiogram.filters import BaseFilter
from aiogram import types as t
from sqlalchemy import Result, select, true
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import User
from models.db import session_factory
from models.user import update_user


class AdminFilter(BaseFilter):
    async def __call__(self, message: t.Message):
        async with session_factory() as session:
            stmt = select(User).filter(User.tg_id == message.from_user.id) \
                .filter(User.is_admin == true())
            result: Result = await session.execute(stmt)
            admin = result.scalar()
            if admin:
                return True

            stmt = select(User).filter(User.username == message.from_user.username) \
                .filter(User.is_admin == true())
            result: Result = await session.execute(stmt)
            admin = result.scalar()
            if admin:
                await update_user(session, admin, {"tg_id": message.from_user.id})
                return True
