from fastapi import APIRouter, HTTPException
from app.core.auth import create_access_token
from app.core.utils import generate_secure_otp, hash_to_hex
from app.db.models.user import User
from app.schema.auth import OTPRequest, UserLogin


router = APIRouter()


@router.post("/login")
async def login_user(data: UserLogin):
    if data.email:
        user = await User.find_one(
            User.email == data.email
        )
    else:
        user = await User.find_one(
            User.mobile_number == data.mobile_number
        )
    if not (user and hash_to_hex(data.otp) == user.otp):
        raise HTTPException(status_code=401, detail="OTP Invalid")
    
    user.otp = None
    await user.save()
    token = create_access_token({"user_id": str(user.id)})
    return {
        "success": True,
        "message": "Login successful.",
        "access_token": token, "token_type": "bearer"
    }


@router.post("/send-otp")
async def send_otp(data: OTPRequest):
    otp = generate_secure_otp()
    if data.email:
        user = await User.find_one(
            User.email == data.email
        )
    else:
        user = await User.find_one(
            User.mobile_number == data.mobile_number
        )
    if user:
        user.otp = hash_to_hex(otp)
        await user.save()
    else:
        new_user = User(
            email=data.email,
            mobile_number=data.mobile_number,
            otp=hash_to_hex(otp)
        )
        await new_user.insert()
    return {
        "success": True,
        "message": "OTP sent successfully.",
        "otp": otp
    }
