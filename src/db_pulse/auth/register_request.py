from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class RegisterRequest(BaseModel):
    name: str | None = None
    username: str
    email: str
    password: str
