from dataclasses import dataclass

from pydantic import BaseModel

from db_pulse.auth.models import User


@dataclass
class LoginRequest(BaseModel):
    username: str
    password: str


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


class Token(BaseModel):
    access_token: str
    token_type: str
