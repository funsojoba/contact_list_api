from rest_framework import serializers
from contact_api.models.contact import ContactModel


class UpdateContactSerailzer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'phone', 'facebook', 'instagram', 'twitter', 'linkedin', 'state']