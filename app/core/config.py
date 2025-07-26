from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str 
    MONGO_DB_NAME: str 
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    GOOGLE_APPLICATION_CREDENTIALS: str
    VERTEX_SERVICE_ID: str
    class Config:
        env_file = ".env"

settings = Settings()
