from rest_framework import serializers
from contact_api.models.email import EmailModel

class SendMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel
        fields = ['sender', 'subject', 'message', 'reciever']
