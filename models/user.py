from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    is_admin: Mapped[bool] = mapped_column(default=False)
    username: Mapped[str]
    tg_id: Mapped[str | None]


async def update_user(session: AsyncSession,
                       user: User, data: Dict[str, str | int]) -> User:
    for name, value in data.items():
        setattr(user, name, value)
    session.add(user)
    await session.commit()
    return user

