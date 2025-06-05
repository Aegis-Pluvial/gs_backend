from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_key: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=str('C:\\Users\\janj\\PycharmProjects\\gs_backend\\.env'),
        env_file_encoding='utf-8'
    )
