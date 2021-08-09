from django.contrib.auth import authenticate

from django.conf import settings

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from .serializer.register import UserSerializer
from .serializer.login_serializer import LoginSerializer
from django.contrib.auth import get_user_model


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('email', '')
            password = data.get('password', '')

            user = get_user_model().objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            user.set_password(password)
            user.save()

            return Response({"data":serializer.data, "message":"success"}, status=status.HTTP_201_CREATED)

        return Response({"error":serializer.errors, "message":"failure"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        if not email or not password:
            return Response({"error":"both email and password are required", "message":"failure"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if not user:
            return Response({"error":"invalid credentials", "message":"failure"}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.serializer_class(user)

        token, _ = Token.objects.get_or_create(user=user)
        
        data = {"message": "success", "token":token.key}

        return Response(data, status=status.HTTP_200_OK)
