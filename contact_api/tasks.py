from celery import shared_task
from typing import Dict, List

from contact_api.helper.send_mail import EmailManager


@shared_task
def send_mail(recipient, subject, template, context):
    mail = EmailManager(
        recipient=recipient, subject=subject, template=template, context=context
    )
    mail.send()


@shared_task
def send_mail_async(template: str, subject: str, recipients: List[str], context: Dict):
    mail = EmailManager(
        template=template, subject=subject, recipients=recipients, context=context
    )
    mail.send()
