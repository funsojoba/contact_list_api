from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from contact_api.serializers.avatar_serializer import AvatarSerializer
from contact_api.models.contact import ContactModel

import cloudinary.uploader
from decouple import config


class AvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ContactModel.objects.all()
    serializer_class = AvatarSerializer

    def post(self, request, pk):
        data = request.data
        contact_user = ContactModel.objects.get(id=pk)
        serializer = AvatarSerializer(data=data)
        serializer.is_valid()

        avatar = data.get('avatar', '')

        if not avatar:
            return Response({"message": "failure", "error": "inavlid file extension"}, status=status.HTTP_400_BAD_REQUEST)

        image_url = ''
        valid_extension = ['jpg', 'png', 'jpeg','svg', 'JPG', 'JPEG']
        avatar_url = serializer.data['avatar']

        if avatar_url.name.split('.')[-1] not in valid_extension:
            return Response({"message": "failure", "error": "inavlid file extension"}, status=status.HTTP_400_BAD_REQUEST)

        upload_image = cloudinary.uploader.upload(
            avatar_url, folder=config('FOLDER_NAME'), user_filename=True, overwrite=True
        )
        image_url += upload_image.get('url')

        contact_user.avatar = image_url
        contact_user.save()

        serializer_dict = dict(serializer.data)
        serializer_dict['avatar'] = image_url
        return Response({"message":"success", "data":serializer_dict}, status=status.HTTP_200_OK)