from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These will be overwritten if they exist in your .env
    PROJECT_NAME: str = Field(default="Fenmo Assessment API", env="PROJECT_NAME")
    VERSION: str = Field(default="1.0.0", env="VERSION")
    DATABASE_URL: str = Field(default="sqlite:///./sql_app.db", env="DATABASE_URL")
    BACKEND_CORS_ORIGINS: list[str] = Field(
        default=["http://localhost:3000"],
        env="BACKEND_CORS_ORIGINS",
    )
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()