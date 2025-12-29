from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
        "env_file_encoding": "utf-8",
    }


config = Config()
