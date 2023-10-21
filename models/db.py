from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import config
from .base import Base

engine = create_async_engine(config.SQLA_DB_URI)
session_factory = async_sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
