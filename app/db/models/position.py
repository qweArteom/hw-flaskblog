from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.db import Base


class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
