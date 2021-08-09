from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from decouple import config

from authenticate.models import User
from contact_api.serializers.user_profile import UserProfileSerializer

import cloudinary.uploader


class UserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = request.user
        queryset = User.objects.get(id=user.id)

        if not queryset:
            return Response({"message": "failure", "error": "user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserProfileSerializer(queryset)
        data = serializer.data
        return Response({"message": "success", "data": data}, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        queryset = User.objects.get(id=user.id)
        data = request.data
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        avatar = data.get('avatar', '')

        serializer = UserProfileSerializer(data=data)
        serializer.is_valid()

        image_url = ''
        if avatar:
            valid_extension = ['jpg', 'png', 'jpeg', 'JPG', 'JPEG', 'svg']
            avatar_url = serializer.data['avatar']

            if avatar_url.name.split('.')[-1] not in valid_extension:
                return Response({"message":"failure", "error":"inavlid file extension"}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_image = cloudinary.uploader.upload(
                avatar_url, folder=config('PROFIL_IMAGE_FOLDER'), user_filename=True, overwrite=True)
            image_url += upload_image.get('url')
        else:
            image_url = queryset.avatar

        queryset.first_name = first_name
        queryset.last_name = last_name
        queryset.avatar = image_url

        queryset.save()
        serializer_dict = dict(serializer.data)
        serializer_dict['avatar'] = image_url

        return Response({"message":"success", "data":serializer_dict}, status=status.HTTP_200_OK)