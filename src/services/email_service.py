from schemas.email_schemas import EmailDataSchema
from services.email_render import HTMLEmailRender
from .email_sender import Email
from configs.config import settings


class EmailService:
    async def send_email(self, user_data: EmailDataSchema) -> None:
        url: str = generate_url(email_type=user_data.email_type, token=user_data.token)

        html = HTMLEmailRender(user_data.username, url).render(user_data.email_type)
        
        user_email_list = [user_data.email]
        email = Email(email=user_email_list)

        res = await email.sendMail(subject=user_data.email_type, html=html)


def generate_url(email_type: str, token: str) -> str:
    return f"{settings.url}/{email_type}/?token={token}"
