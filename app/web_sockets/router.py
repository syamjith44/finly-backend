from fastapi import APIRouter
from app.web_sockets.endpoints import assistant


router = APIRouter()


router.include_router(assistant.router, prefix="/assistant", tags=["Assistant"])