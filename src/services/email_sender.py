from typing import List
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from configs.config import settings


subjects_dict = {
    "verification": "Подтверждение регистрации",
    "reset": "Восстановление входа"
}


class Email:
    def __init__(self, email: List[str]) -> None:
        self.email = email

    async def sendMail(self, subject: str, html: str) -> None:
        conf = ConnectionConfig(
            MAIL_USERNAME=settings.email.username,
            MAIL_PASSWORD=settings.email.password,
            MAIL_FROM=settings.email.from_email,
            MAIL_PORT=settings.email.port,
            MAIL_SERVER=settings.email.host,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=True,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True
        )

        message = MessageSchema(
            subject=subjects_dict.get(subject),
            recipients=self.email,
            body=html,
            subtype="html"
        )

        fm = FastMail(conf)
        await fm.send_message(message)
