from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_key: str
    database_url: str
    debug_mode: bool

    model_config = SettingsConfigDict(
        env_file="app/.env.local",
        env_file_encoding="utf-8",
    )

settings = Settings()
print(f"DEBUG: Loaded DATABASE_URL: {settings.database_url}")