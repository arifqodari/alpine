from pydantic_settings import BaseSettings
from pydantic import Field


class GeneralSettings(BaseSettings):
    is_debug: bool = Field(default=True)


class GunicornSettings(BaseSettings):
    gunicorn_num_workers: int = 2
    gunicorn_num_threads: int = 1
    gunicorn_timeout: int = 30


general_settings = GeneralSettings()
gunicorn_settings = GunicornSettings()


if __name__ == "__main__":
    print(general_settings.model_dump())
    print(gunicorn_settings.model_dump())