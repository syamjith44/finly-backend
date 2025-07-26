from pathlib import Path
from app.core.config import settings

cred_path = Path(settings.GOOGLE_APPLICATION_CREDENTIALS)
if not cred_path.exists():
    raise FileNotFoundError(f"Vertex AI credentials file not found at: {cred_path}")