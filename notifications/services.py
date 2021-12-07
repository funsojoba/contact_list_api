from typing import List, Dict
from notifications.tasks import send_mail_async
from contact_api.models.email import EmailModel

class EmailService:
    @classmethod
    def send_email(cls, template: str, subject: str, recipients: List[str], context: Dict, sender: str):
        send_mail_async.delay(
            template=template, 
            subject=subject, 
            recipients=recipients, 
            context=context
        )

        EmailModel.objects.create(
            sender=sender,
            subject=subject,
            message=context["message"],
            reciever=recipients[0],
        )
