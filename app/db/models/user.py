from typing import Optional
from app.db.models.abstract import BaseDocument

class User(BaseDocument):
    email: Optional[str] = None
    mobile_number: Optional[str] = None
    otp: Optional[str] = None

    class Settings:
        name = "users"
