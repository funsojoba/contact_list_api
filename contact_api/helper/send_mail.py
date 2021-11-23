from decouple import config
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class EmailManager:
    def __init__(self, recipient, template, context, subject):
        self.recipient = recipient
        self.subject = subject
        self.template = template
        self.context = context
    
    def _compose_mail(self):
        message = EmailMessage(
            to=self.recipient,
            subject=self.subject,
            body=render_to_string(self.template, self.context)
        )
        message.content_subtype = "html"
        return message
    
    def send(self):
        mail = self._compose_mail()
        result = mail.send(fail_silently=False)
        return result
