from pydantic import BaseSettings
import argparse
from functools import lru_cache
from dotenv import find_dotenv
from enum import Enum

__all__ = ['get_settings']


class RunType(Enum):
    DEV = "dev"
    PROD = "prod"

    def __str__(self):
        return self.value


class _Setting(BaseSettings):
    class Config:
        env_file: str
        env_file_encoding = "utf-8"


class Setting(_Setting):
    # server
    HOST: str
    PORT: int
    WORKER: int

    # auth
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    # redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_DATABASE: str

    CRYPT_KEY: str
    JWT_SECRET: str

    # cli_args
    REFLECTOR: bool = False


# Parsing arg in command line
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", choices=RunType, type=RunType)
    parser.add_argument("base_block", nargs="?", default=None, type=int)
    args = parser.parse_args()
    return args


@lru_cache()
def get_settings() -> Setting:
    args = arg_parser()
    type_of_worker = RunType(args.type)
    settings = Setting(
        _env_file=find_dotenv(
            ".env" if type_of_worker == ".env.prod" else ".env.dev"
        ),
    )
    settings.REFLECTOR = True if type_of_worker == RunType.DEV else False
    print(settings)
    return settings
