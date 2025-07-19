from bson import ObjectId
from fastapi import APIRouter, Depends

from app.api.dependancies import JWTBearer
from app.db.models.user import User
from app.schema.auth import TokenPayload


router = APIRouter()


@router.get("/user-settings",)
async def user_settings(
    token_payload: dict = Depends(JWTBearer())
):
    data = TokenPayload(**token_payload)
    user = await User.find_one(
        User.id == ObjectId(data.user_id)
    )
    return user
