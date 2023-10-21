from typing import List, Optional

from sqlalchemy import select, Result
from sqlalchemy.orm import Mapped, relationship

from models import Base
from models.db import session_factory


class Message(Base):
    text: Mapped[str]

    actions: Mapped[List["Action"]] = relationship(back_populates='message')


async def get_message_by_text(text: str) -> Optional[Message]:
    async with session_factory() as session:
        stmt = select(Message).filter(Message.text == text)
        result: Result = await session.execute(stmt)
        message: Message = result.scalar()
    return message
