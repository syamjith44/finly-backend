import json
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Query, WebSocket, WebSocketDisconnect

from app.api.dependancies import JWTBearer
from app.core.auth import decode_access_token
from app.db.models.user import User
from app.schema.auth import TokenPayload


router = APIRouter()


@router.websocket("/chat")
async def websocket_endpoint(
    websocket: WebSocket, token: str = Query(...)
):
    try:
        token_payload = decode_access_token(token)
        data = TokenPayload(**token_payload)
    except HTTPException:
        await websocket.close(code=1008)(token)
        return
    user = await User.find_one(
        User.id == ObjectId(data.user_id)
    )
    if not user:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            data["message"] = f"You said {data["message"]}"
            await websocket.send_text(f"{json.dumps(data)}")
    except WebSocketDisconnect:
        print(f"Client {token} disconnected")
        