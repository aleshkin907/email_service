import os
import yaml

from pydantic import BaseModel

from schemas.settings_schemas import EmailSettingsSchema


class Settings(BaseModel):
    email: EmailSettingsSchema
    url: str


def load_config():
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(os.path.dirname(current_dir)).strip("/")
    config_file  = "/" + parent_dir + "/config.yaml"
    with open(config_file, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return Settings(**config)

settings = load_config()
