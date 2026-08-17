from dataclasses import dataclass

from pydantic import BaseModel

from db_pulse.auth.user import User


@dataclass
class RegisterRequest(BaseModel):
    name: str | None = None
    username: str
    email: str
    password: str

    def to_user(self) -> User:
        """Maps the request data to a SQLAlchemy User instance."""
        return User(
            name=self.name,
            username=self.username,
            email=self.email,
            password=self.password,
        )
