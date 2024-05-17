from typing import Literal
from pydantic import BaseModel


class EmailDataSchema(BaseModel):
    email_type: Literal["verification", "reset"]
    username: str
    email: str
    token: str
    