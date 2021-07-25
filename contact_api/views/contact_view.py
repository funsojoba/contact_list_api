from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from decouple import config

import cloudinary.uploader

from contact_api.serializers.contact_serializer import ContactSerializer
from contact_api.models.contact import ContactModel


class Contact(APIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        twitter = data.get('twitter', '')
        instagram = data.get('instagram')
        facebook = data.get('facebook', '')
        linkedin = data.get('linkedin', '')
        state = data.get('state', '')
        avatar = data.get('avatar', '')

        serializer = self.serializer_class(data=data)

        serializer.is_valid()

        image_url = ''
        if avatar:
            valid_extension = ['jpg', 'gif', 'png',
                               'jpeg', 'svg', 'JPG', 'JPEG']
            avatar_url = serializer.data['avatar']
            print(serializer.data)
            if avatar_url.name.split('.')[-1] not in valid_extension:
                return Response({"error": "invalid file format"}, status=status.HTTP_400_BAD_REQUEST)

            upload_image = cloudinary.uploader.upload(avatar_url, folder=config(
                'FOLDER_NAME'), user_filename=True, overwrite=True)
            image_url += upload_image.get('url')
        else:
            image_url += "https://res.cloudinary.com/ddl2pf4qh/image/upload/v1623512852/24-248253_user-profile-default-image-png-clipart-png-download_qwj0qi.png"

        contact = ContactModel.objects.create(
            owner=user,
            first_name=first_name, last_name=last_name, email=email, facebook=facebook,
            phone=phone, twitter=twitter, instagram=instagram, linkedin=linkedin, state=state, avatar=image_url)
        contact.save()

        serializer_dict = dict(serializer.data)
        serializer_dict['avatar'] = image_url

        return Response(serializer_dict, status=status.HTTP_201_CREATED)
