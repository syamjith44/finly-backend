from bson import ObjectId
from fastapi import APIRouter, Depends, Request

from app.ai_core.vertex.api import ask_gemini
from app.api.dependancies import JWTBearer
from app.db.models.user import User
from app.schema.assistant import PromptRequest
from app.schema.auth import TokenPayload


router = APIRouter()


@router.post("/ask-gemini/")
def ask_gemini_handler(
    request: Request,
    payload: PromptRequest
):
    client = request.app.state.gemini_client
    response = ask_gemini(client, payload.prompt)
    return {"response": response}


@router.get("/chat")
async def chat(
    token_payload: dict = Depends(JWTBearer())
):
    data = TokenPayload(**token_payload)
    user = await User.find_one(
        User.id == ObjectId(data.user_id)
    )
    return []
