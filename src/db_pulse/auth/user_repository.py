from pydantic import BaseModel
from sqlalchemy import select

from db_pulse.auth.models import User
from db_pulse.database.sessions import SessionLocal


class UserRepository(BaseModel):
    def add_user(self, user: User) -> User:
        with SessionLocal() as session:
            with session.begin():
                session.add(user)

            session.refresh(user)

        return user

    def find_user_by_username(self, username: str) -> User | None:
        with SessionLocal() as session:
            statement = select(User).where(User.username == username)
            user = session.scalar(statement)

            if not user:
                return None

            return user
