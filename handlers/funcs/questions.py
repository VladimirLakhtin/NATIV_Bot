from typing import Dict

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import Question


async def get_questions(session_factory: async_sessionmaker) -> list[Question]:
    async with session_factory() as session:
        stmt = select(Question).order_by(Question.id)
        result: Result = await session.execute(stmt)
        questions = result.scalars().all()
    return list(questions)


async def create_question(session_factory: async_sessionmaker,
                          data: Dict[str, str]) -> None:
    async with session_factory() as session:
        question = Question(**data)
        session.add(question)
        await session.commit()


async def get_question_by_id(session_factory: async_sessionmaker,
                             id: int) -> Question:
    async with session_factory() as session:
        stmt = select(Question).filter(Question.id == id).order_by(Question.id)
        result: Result = await session.execute(stmt)
        question = result.scalar()
    return question


async def update_question(session_factory: async_sessionmaker,
                          id: int, data: Dict[str, str]) -> Question:
    async with session_factory() as session:
        question = await get_question_by_id(session_factory, id)
        for name, value in data.items():
            setattr(question, name, value)
        session.add(question)
        await session.commit()
    return question


async def delete_question(session_factory: async_sessionmaker,
                          id: int) -> None:
    async with session_factory() as session:
        question = await get_question_by_id(session_factory, id)
        await session.delete(question)
        await session.commit()
