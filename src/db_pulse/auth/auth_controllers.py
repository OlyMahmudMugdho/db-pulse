from datetime import timedelta

from fastapi import APIRouter, HTTPException, status
from pwdlib import PasswordHash

from db_pulse.auth.login_request import LoginRequest
from db_pulse.auth.register_request import RegisterRequest
from db_pulse.auth.token import Token
from db_pulse.auth.user_repository import UserRepository
from db_pulse.auth.utils import create_access_token
from db_pulse.configs.jwt_config import JWTConfig

router = APIRouter()

user_repository = UserRepository()

password_hash = PasswordHash.recommended()


@router.post("/register")
async def register(request: RegisterRequest):
    hashed_password = password_hash.hash(request.password)
    request.password = hashed_password

    if user_repository.find_user_by_username(request.username):
        return

    user = request.to_user()
    return user_repository.add_user(user)


@router.post("/login")
async def login(request: LoginRequest):
    user = user_repository.find_user_by_username(request.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not password_hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=JWTConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")
