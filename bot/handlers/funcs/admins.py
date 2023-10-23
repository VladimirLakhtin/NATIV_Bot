from typing import List

from sqlalchemy import select, true, Result
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import User


async def get_admins(session_factory: async_sessionmaker) -> List[User]:
    async with session_factory() as session:
        stmt = select(User).filter(User.is_admin == true())
        result: Result = await session.execute(stmt)
        return list(result.scalars())
