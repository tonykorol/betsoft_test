from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path, override=True)

class Settings(BaseSettings):
    MODE: str

    BET_MAKER_URL: str = "http://bet-maker:8002"

    model_config = SettingsConfigDict(env_file=env_path)

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
