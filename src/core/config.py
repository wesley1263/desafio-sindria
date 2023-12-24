from functools import lru_cache

from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI = config("MONGO_URI")
    MONGO_DB = config("MONGO_DB")
    APP_NAME = config("APP_NAME", default="Sindria")
    APP_VERSION = config("APP_VERSION", default="1.0.0")
    APP_DESCRIPTION = config("APP_DESCRIPTION", default="Desafio Sindria")
    ROOT_PATH = config("ROOT_PATH", default="/")
    TESTING = config("TESTING", default=True, cast=bool)


@lru_cache()
def get_settings():
    return Settings()
