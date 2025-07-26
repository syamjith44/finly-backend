from fastapi import APIRouter
from app.api.v1.endpoints import assistant, auth, users

router = APIRouter()

# Group auth routes
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(assistant.router, prefix="/assistant", tags=["Assistant"])