from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, Result, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.db import session_factory


class Action(Base):
    is_message: Mapped[bool]
    date: Mapped[datetime] = mapped_column(default=datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    question_id: Mapped[int | None] = mapped_column(ForeignKey('questions.id'))
    message_id: Mapped[int | None] = mapped_column(ForeignKey('messages.id'))

    user: Mapped["User"] = relationship(back_populates="actions", lazy='joined')
    question: Mapped["Question"] = relationship(back_populates='actions', lazy='joined')
    message: Mapped["Message"] = relationship(back_populates='actions', lazy='joined')


async def get_actions() -> List[Action]:
    async with session_factory() as session:
        stmt = select(Action).order_by(Action.user_id, Action.date)
        result: Result = await session.execute(stmt)
        actions = result.scalars()
    return list(actions)
