from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from models import Question


async def get_questions(session_factory: async_sessionmaker) -> list[Question]:
    async with session_factory() as session:
        stmt = select(Question).order_by(Question.id)
        result: Result = await session.execute(stmt)
        questions = result.scalars().all()
    return list(questions)
