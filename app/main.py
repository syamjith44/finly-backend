from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.db.mongodb import connect_to_mongo
from app.api.v1.api_router import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield


app = FastAPI(
    title="Finly AI API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Register your versioned API router
app.include_router(api_router, prefix="/api/v1")
