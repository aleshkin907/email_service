from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api_v1.dependencies import email_service
from schemas.email_schemas import EmailDataSchema
from services.email_service import EmailService


router = APIRouter(prefix="/email", tags=["email"])

@router.post("/")
async def send_email_to_user(
    email_data: EmailDataSchema,
    email_service: EmailService = Depends(email_service),
) -> JSONResponse:
    send_email_to_user = await email_service.send_email(email_data)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Email sent"})
