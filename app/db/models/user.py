from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from app.db import Base, Position


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[int] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(nullable=True)
    position_id: Mapped[int] = mapped_column(ForeignKey(Position.id))
