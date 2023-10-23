from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Flag(Base):
    name: Mapped[str]
    value: Mapped[bool] = mapped_column(default=True)
