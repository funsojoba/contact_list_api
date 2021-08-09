from rest_framework import serializers
from contact_api.models.contact import ContactModel


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['avatar']