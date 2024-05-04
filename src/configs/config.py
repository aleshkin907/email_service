from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings

from schemas.settings_schemas import AppSettingsSchema, EmailSettingsSchema


class Settings(YamlBaseSettings):
    app: AppSettingsSchema
    email: EmailSettingsSchema
    url: str

    class Config:
        yaml_file = "config.yaml"
        ignore_extra = True

settings = Settings()
