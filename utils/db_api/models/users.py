from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from utils.db_api.base import Base
from typing import Optional



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[Optional[str]] = mapped_column(String)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    banned: Mapped[int] = mapped_column(Integer, default=0)
    time_start: Mapped[int] = mapped_column(BigInteger, default=0)