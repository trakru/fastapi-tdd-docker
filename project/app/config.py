import logging
import os

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

#change value sin powershell using the $env:env=new value notation
# $env:ENVIRONMENT='prod'

def get_settings() -> BaseSettings:
    log.info("Loading config settings from environment...")
    return Settings()