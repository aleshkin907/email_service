from typing import Literal
from pydantic import BaseModel


class EmailDataSchema(BaseModel):
    username: str
    email: str
    token: str
    