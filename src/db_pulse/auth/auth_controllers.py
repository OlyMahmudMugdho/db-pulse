from fastapi import APIRouter
from pwdlib import PasswordHash

from db_pulse.auth.register_request import RegisterRequest
from db_pulse.auth.user_repository import UserRepository

router = APIRouter()

user_repository = UserRepository()


@router.post("/register")
async def register(request: RegisterRequest):
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(request.password)
    request.password = hashed_password

    if user_repository.find_user_by_username(request.username):
        return None

    user = request.to_user()
    return user_repository.add_user(user)
