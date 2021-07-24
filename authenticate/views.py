import jwt

from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import status
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

        user = User.objects.get(username=username)
        
        if not user:
            raise AuthenticationFailed("User does not exist")

        
        user_password = user.check_password(password)
        if not user_password:
            raise AuthenticationFailed("incorrect password")

        auth_token = jwt.encode(
            {"username": user.username}, settings.JWT_SECRET_KEY)
        
        data = {"user": self.serializer_class.data, "token":auth_token}
            # serializer = UserSerializer(user)

            # data = {
            #     'user':serializer.data,
            #     'token': auth_token
            # }
        return Response(data, status=status.HTTP_200_OK)
