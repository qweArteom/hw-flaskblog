from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, TEXT, ForeignKey
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func

from app.db import Base, User


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    text: Mapped[str] = mapped_column(TEXT())
    create: Mapped[datetime] = mapped_column(TIMESTAMP(), server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
