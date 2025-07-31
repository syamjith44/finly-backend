from google import genai
from google.genai.types import HttpOptions


def create_client():
    return genai.Client(
        vertexai=True, 
        project="finly-vertex-api", 
        location="us-central1",
        http_options=HttpOptions(api_version="v1")
    )


def ask_gemini(client, prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
