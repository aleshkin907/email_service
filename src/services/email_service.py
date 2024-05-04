from schemas.email_schemas import EmailDataSchema
from services.email_render import HTMLEmailRender
from .email_sender import Email
from configs.config import settings


class EmailService:
    async def send_email(self, mail_type: str, user_data: EmailDataSchema) -> None:
        url: str = generate_url(mail_type=mail_type, token=user_data.token)

        html = HTMLEmailRender(user_data.username, url).render(mail_type)
        
        user_email_list = [user_data.email]
        email = Email(email=user_email_list)

        res = await email.sendMail(subject=mail_type, html=html)


def generate_url(mail_type: str, token: str) -> str:
    return f"{settings.url}/{mail_type}/?token={token}"
