from pydantic import BaseModel


class AppSettingsSchema(BaseModel):
    host: str
    port: int

class EmailSettingsSchema(BaseModel):
    username: str
    password: str
    from_email: str
    port: int
    host: str
