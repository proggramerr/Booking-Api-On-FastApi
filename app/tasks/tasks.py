import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def hadler_pic(
    path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_big = im.resize((1000, 500))
    im_resized_small = im.resize((600, 400))
    im_resized_big.save(f'app/static/images/resized_1000_500_{im_path.name}')
    im_resized_small.save(f'app/static/images/resized_600_4 00_{im_path.name}')

@celery.task
def send_booking_confirmation_email(
    booking:dict,
    email_to: EmailStr,
):
    email_to_mock = 'nonamers1338@mail.ru'
    msg_content = create_booking_confirmation_template(booking, email_to_mock)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)