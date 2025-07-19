from datetime import datetime, timedelta, timezone
import secrets
import hashlib
from jose import JWTError, jwt

from app.core.config import settings


def generate_secure_otp(length=6):
    digits = "0123456789"
    return ''.join(secrets.choice(digits) for _ in range(length))


def hash_to_hex(raw_value: str):
    return hashlib.sha256(raw_value.encode()).hexdigest()
