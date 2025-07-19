import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import hashlib

async def insert_user():
    client = AsyncIOMotorClient(
        "mongodb+srv://finlyaiglobal:G9y4uGfayyJg2pC5@finly-cluster."
        "evcvnop.mongodb.net/?retryWrites=true&w=majority&appName=finly-cluster"
    )
    db = client["finly-test-db"]
    await db["users"].insert_one({
        "username": "admin",
        "email": "admin@finly.ai",
        "mobile_number": "9400049791",
        "country_code": "+91",
        "hashed_password": hashlib.sha256("password".encode()).hexdigest()
    })
    print("✅ User added")

asyncio.run(insert_user())
