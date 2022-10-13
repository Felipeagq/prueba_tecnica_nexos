import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    # PROJECT INFO
    PROJECT_NAME:str ="Prueba Tecnica Nexos"
    PROJECT_VERSION:str ="v0.0.1"
    API_V1_STR:str = "/api/v1"
    
    # POSTGRES GENERAL CREDENTIALS
    _PG_NAME: str = os.getenv("PG_NAME") or None
    _PG_USER: str = os.getenv("PG_USER") or None
    _PG_PASSWORD: str = os.getenv("PG_PASSWORD") or None
    _PG_HOST: str = os.getenv("PG_HOST") or None
    _PG_PORT:str = os.getenv("PG_PORT") or None
    
    # POSTGRES DATABASE URL CONSTRUCTION
    SQLALCHEMY_DATABASE_URL: str = f"postgresql://{_PG_USER}:{_PG_PASSWORD}@{_PG_HOST}:{_PG_PORT}"



settings = Settings()