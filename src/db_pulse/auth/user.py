from tokenize import String

from sqlalchemy.orm import Mapped, mapped_column

from db_pulse.configs.sqlalchemy_base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
