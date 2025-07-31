from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import vertexai
from contextlib import asynccontextmanager

from app.db.mongodb import connect_to_mongo
from app.api.api_router import router as api_router
from app.web_sockets.router import router as web_socket_router
from app.ai_core.vertex.api import create_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    app.state.gemini_client = create_client()
    yield


app = FastAPI(
    title="Finly AI API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000", "ws://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Register your versioned API router
app.include_router(api_router, prefix="/api")
app.include_router(web_socket_router, prefix="/ws")
