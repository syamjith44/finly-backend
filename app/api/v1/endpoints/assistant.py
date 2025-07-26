from fastapi import APIRouter

from app.ai_core.vertex.api import ask_gemini
from app.schema.assistant import PromptRequest


router = APIRouter()


@router.post("/ask-gemini/")
def ask_gemini_handler(request: PromptRequest):
    response = ask_gemini(request.prompt)
    return {"response": response}