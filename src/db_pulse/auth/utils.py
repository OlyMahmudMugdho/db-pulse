from datetime import UTC, datetime, timedelta

import jwt

from db_pulse.configs.jwt_config import JWTConfig


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, JWTConfig.SECRET_KEY, algorithm=JWTConfig.ALGORITHM
    )
    return encoded_jwt
