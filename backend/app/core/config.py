from pydantic import Field, field_validator
from typing import List, Union
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These will be overwritten if they exist in your .env
    PROJECT_NAME: str = Field(default="Fenmo Assessment API", env="PROJECT_NAME")
    VERSION: str = Field(default="1.0.0", env="VERSION")
    DATABASE_URL: str = Field(default="sqlite:///./sql_app.db", env="DATABASE_URL")
    BACKEND_CORS_ORIGINS: List[str] = []
    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        return []

settings = Settings()