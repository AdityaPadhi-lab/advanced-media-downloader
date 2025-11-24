from pydantic_settings import BaseSettings, SettingsConfigDict

class BotSettings(BaseSettings):
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
    SESSION_STRING: str = ""
    REDIS_URL: str = "redis://redis:6379/0"
    BACKEND_URL: str = "http://server:8000"

    model_config = SettingsConfigDict(
        env_file="../infra/.env",
        extra="allow"
    )

settings = BotSettings()
