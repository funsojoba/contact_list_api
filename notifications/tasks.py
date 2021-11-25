import smtplib
from django.conf import settings
from celery import shared_task

from notifications.utils import EmailManager


@shared_task(
    bind=True,
    autoretry_for=(smtplib.SMTPException,),
    retry_kwargs={
        "max_retries": settings.CELERY_MAX_RETRY,
        "countdown": settings.CELERY_RETRY_DELAY,
    },
)
def send_mail_async():
    pass

