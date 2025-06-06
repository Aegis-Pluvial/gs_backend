from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AI_api_key: str
    api_key: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=str('C:\\Users\\janj\\PycharmProjects\\gs_backend\\.env'),
        env_file_encoding='utf-8'
    )
