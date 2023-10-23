from typing import List

from sqlalchemy.orm import Mapped, relationship

from .base import Base


class Question(Base):
    question: Mapped[str]
    answer: Mapped[str]

    actions: Mapped[List["Action"]] = relationship(back_populates="question")
