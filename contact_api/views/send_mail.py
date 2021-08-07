from decouple import config

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import get_template
from contact_api.models.contact import ContactModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from contact_api.serializers.send_mail_serializer import SendMailSerializer
from contact_api.models.email import EmailModel


def send_mail(name, subject, message, to, from_email, sender):
    html_path = 'email_template/welcome.html'
    context_data = {'name': name, 'subject': subject, 'message': message, 'sender':sender}
    email_template = get_template(html_path).render(context_data)
    email_message = EmailMessage(
        subject=subject,
        body=email_template,
        from_email=from_email,
        to=[to])
    email_message.content_subtype = 'html'
    email_message.send(fail_silently=False)


class SendMail(APIView):
    serializer_class = SendMailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        data = request.data
        query = ContactModel.objects.get(id=pk)

        data['sender'] = request.user.id

        sender = request.user
        message = data.get('message', '')
        subject = data.get('subject', '')

        reciever_email = query.email
        reciever_name = query.first_name

        data['reciever'] = reciever_email

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.data['sender'] = sender

        if not query.email:
            return Response({"message":"failure", "error":"user email does not exist"})

        try:
            send_mail(name=reciever_name, subject=subject, message=message,
                  to=reciever_email, from_email=config('EMAIL_HOST_USER'), sender=sender.email)
        except Exception as err:
            # return Response({"error":err, "message":"failure"}, status=status.HTTP_400_BAD_REQUEST)
            print(err)
        
        create_db_email = EmailModel.objects.create(sender=sender, subject=subject, message=message, reciever=reciever_email)
        create_db_email.save()

        return Response({"message":"success", "data":serializer.data, "info":f'Message sent to {reciever_email}'})
