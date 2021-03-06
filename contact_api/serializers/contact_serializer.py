from rest_framework import serializers
from contact_api.models.contact import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['owner', 'first_name', 'last_name', 'email', 'phone', 'twitter', 'facebook', 'instagram', 'linkedin', 'state']
