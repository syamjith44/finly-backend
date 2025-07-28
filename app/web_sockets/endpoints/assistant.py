from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect

from app.api.dependancies import JWTBearer
from app.db.models.user import User
from app.schema.auth import TokenPayload


router = APIRouter()


@router.websocket("/ws/chat/{token}")
async def websocket_endpoint(
    websocket: WebSocket, token: str
):
    try:
        token_payload = Depends(JWTBearer())
        data = TokenPayload(**token_payload)
    except HTTPException:
        await websocket.close(code=1008)(token)
        return
    user = await User.find_one(
        User.id == ObjectId(data.user_id)
    )
    if not user:
        await websocket.close(code=1008)(token)
        return
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print(f"Client {token} disconnected")
        