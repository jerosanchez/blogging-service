import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Always use the CWD to find the .env at the project root
env_path = os.path.join(os.getcwd(), ".env")

# Only load .env if it exists
if os.path.exists(env_path):
    load_dotenv(env_path)


class Config(BaseSettings):
    app_name: str = "Blogging Service"
    debug: bool = False

    postgres_user: str = "user"
    postgres_password: str = "password"
    postgres_host: str = "db"
    postgres_db: str = "db"

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:5432/{self.postgres_db}"
        )

    model_config = {
        "env_file": env_path,
        "extra": "ignore",
        "env_file_encoding": "utf-8",
    }


config = Config()
