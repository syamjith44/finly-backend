from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from beanie import init_beanie

from app.db.models.user import User


client: AsyncIOMotorClient = None


async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)
    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[
            User
        ]
    )

def get_database():
    return client[settings.MONGO_DB_NAME]
