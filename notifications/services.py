from notifications.tasks import send_mail_async
from contact_api.models.email import EmailModel


def send_email(template, subject, recipients, context, sender, receiver):
    send_mail_async.delay(template=template, subject=subject, recipients=recipients, context=context)
    EmailModel.objects.create(sender=sender, subject=subject, message=context['message'], reciever=receiver)
        