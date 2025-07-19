from typing import Union
from pydantic import BaseModel, EmailStr


class OTPRequest(BaseModel):
    email: Union[EmailStr, None] = None
    mobile_number: Union[str, None] = None


class UserLogin(OTPRequest):
    otp: str
    

class TokenPayload(BaseModel):
    user_id: str