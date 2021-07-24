from django.contrib.auth import authenticate

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import AuthenticationFailed

from .serializer.register import UserSerializer
from .serializer.login_serializer import LoginSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        if not username:
            return Response({"error":"username is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error":"invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.serializer_class(user)

        token, _ = Token.objects.get_or_create(user=user)
        
        data = {"message": "success", "token":token.key}

        return Response(data, status=status.HTTP_200_OK)
