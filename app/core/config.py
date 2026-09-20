from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    watch_paths: List[str] = []
    output_path: str = './output'
    excel_template: str = 'template.xlsx'
    log_level: str = 'INFO'
    database_url: str = 'sqlite:///./automator.db'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()