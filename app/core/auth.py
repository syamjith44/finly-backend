from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.core.config import settings


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY, 
        algorithm="HS256"
    )


def decode_access_token(token: str):
    try:
        return jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=["HS256"])
    except JWTError:
        return None