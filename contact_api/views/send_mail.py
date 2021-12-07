from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from contact_api.models.contact import ContactModel
from contact_api.serializers.send_mail_serializer import SendMailSerializer

from notifications.services import EmailService


class SendMail(APIView):
    serializer_class = SendMailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        data = request.data
        query = ContactModel.objects.get(id=pk)

        data["sender"] = request.user.id

        sender = request.user
        message = data.get("message", "")
        subject = data.get("subject", "")

        reciever_email = query.email
        reciever_name = query.first_name

        data["reciever"] = reciever_email

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.data["sender"] = sender

        if not query.email:
            return Response(
                {"message": "failure", "error": "user email does not exist"}
            )

        context = {"message": message, "receiver": reciever_name}
        EmailService.send_email(
            template='email_template.html',
            subject=subject,
            recipients=[reciever_email],
            sender=sender,
            context=context,
        )

        return Response(
            {
                "message": "success",
                "data": serializer.data,
                "info": f"Message sent to {reciever_email}",
            }
        )
