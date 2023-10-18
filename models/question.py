from sqlalchemy.orm import Mapped

from .base import Base


class Question(Base):
    question: Mapped[str]
    answer: Mapped[str]
