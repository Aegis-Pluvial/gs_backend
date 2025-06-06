from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Pydantic Settings. Monta um objeto Settings que facilita a extração de dados do dotenv
class Settings(BaseSettings):
    AI_api_key: str
    api_key: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / '.env',
        env_file_encoding='utf-8'
    )
