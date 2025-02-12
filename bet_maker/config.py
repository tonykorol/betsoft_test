import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path, override=True)


class Settings(BaseSettings):
    MODE: str

    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    LINE_PROVIDER_URL: str = "http://line-provider:8001"

    model_config = SettingsConfigDict(env_file=env_path)

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
