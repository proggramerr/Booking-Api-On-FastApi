from typing import Literal

from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']

    DB_HOST: str
    DB_PORT: int
    DB_USER: str 
    DB_PASS: str
    DB_NAME: str

    @root_validator
    def get_database_url(cls, values):
        values['DATABASE_URL'] = f'postgresql+asyncpg://{values["DB_USER"]}:{values["DB_PASS"]}@{values["DB_HOST"]}:{values["DB_PORT"]}/{values["DB_NAME"]}'
        return values

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @root_validator
    def get_test_database_url(cls, values):
        values['TEST_DATABASE_URL'] = f'postgresql+asyncpg://{values["TEST_DB_USER"]}:{values["TEST_DB_PASS"]}@{values["TEST_DB_HOST"]}:{values["TEST_DB_PORT"]}/{values["TEST_DB_NAME"]}'
        return values

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str
    ALGHORITM: str
    
    LOG_LEVEL: str

    class Config:
        env_file = '.env'

settings = Settings()
print(settings.DATABASE_URL)