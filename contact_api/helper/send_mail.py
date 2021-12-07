from typing import List
from decouple import config
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string



class EmailManager:
    def __init__(self, recipients, template, context, subject):
        self.recipients = recipients
        self.subject = subject
        self.template = template
        self.context = context
    
    def _compose_mail(self):
        message = EmailMessage(
            subject=self.subject,
            body=render_to_string(self.template, self.context),
            from_email=self.from_email,
            to=self.recipients,
        )
        message.content_subtype = "html"
        return message
    
    def send(self):
        mail = self._compose_mail()
        result = mail.send(fail_silently=False)
        return result

class SendEmail:
    def __init__(self, subject: str, body: str, email_from: str, email_to: List):
        pass