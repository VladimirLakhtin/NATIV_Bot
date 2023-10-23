from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import Flag


async def check_consultation_available(session_factory: async_sessionmaker) -> bool:
    async with session_factory() as session:
        stmt = select(Flag).filter(Flag.name == 'consultation')
        result: Result = await session.execute(stmt)
        flag = result.scalar()
    return flag.value


async def change_consultation_available(session_factory: async_sessionmaker) -> bool:
    async with session_factory() as session:
        stmt = select(Flag).filter(Flag.name == 'consultation')
        result: Result = await session.execute(stmt)
        flag = result.scalar()
        flag.value = not flag.value
        session.add(flag)
        await session.commit()
        return flag.value


async def check_lesson_available(session_factory: async_sessionmaker) -> bool:
    async with session_factory() as session:
        stmt = select(Flag).filter(Flag.name == 'lesson')
        result: Result = await session.execute(stmt)
        flag = result.scalar()
    return flag.value


async def change_lesson_available(session_factory: async_sessionmaker) -> bool:
    async with session_factory() as session:
        stmt = select(Flag).filter(Flag.name == 'lesson')
        result: Result = await session.execute(stmt)
        flag = result.scalar()
        flag.value = not flag.value
        session.add(flag)
        await session.commit()
        return flag.value
