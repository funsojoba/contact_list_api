from rest_framework import serializers
from contact_api.models.contact import ContactModel


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'
