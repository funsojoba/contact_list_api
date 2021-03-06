from rest_framework import serializers
from authenticate.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=85, write_only=True, min_length=8)
    email = serializers.EmailField(min_length=4, max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"email error":"email already exist"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)