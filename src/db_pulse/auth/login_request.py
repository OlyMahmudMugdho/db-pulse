from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class LoginRequest(BaseModel):
    username: str
    password: str
