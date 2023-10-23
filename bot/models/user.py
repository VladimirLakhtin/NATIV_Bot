from typing import Dict, List, Optional

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .db import session_factory


class User(Base):
    username: Mapped[str]
    tg_id: Mapped[str | None]
    is_admin: Mapped[bool] = mapped_column(default=False)

    actions: Mapped[List["Action"]] = relationship(
        back_populates="user", cascade="all")


async def get_user_by_tg_id(tg_id: int) -> Optional[User]:
    async with session_factory() as session:
        stmt = select(User).filter(User.tg_id == tg_id)
        result: Result = await session.execute(stmt)
        message: User = result.scalar()
    return message


async def update_user(session: AsyncSession,
                       user: User, data: Dict[str, str | int]) -> User:
    for name, value in data.items():
        setattr(user, name, value)
    session.add(user)
    await session.commit()
    return user
