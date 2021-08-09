
from rest_framework import serializers
from authenticate.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=250, read_only=True)
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'email']
