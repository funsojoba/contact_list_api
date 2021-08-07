from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from contact_api.models.contact import ContactModel
from contact_api.serializers.contact_list_serializer import ContactListSerializer

from decouple import config
import cloudinary.uploader


class UpdateContactView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ContactModel.objects.all()
    serializer_class = ContactListSerializer

    def put(self, request, pk):
        data = request.data
        # ---------------------
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        facebook = data.get('facebook', '')
        instagram = data.get('instagram', '')
        twitter = data.get('twitter', '')
        linkedin = data.get('linkedin', '')
        state = data.get('state', '')
        avatar = data.get('avatar', '')

        db_data = ContactModel.objects.get(id=pk)
        serializer = ContactListSerializer(data=data)
        serializer.is_valid()

        if not first_name:
            first_name = db_data.first_name

        if not last_name:
            last_name = db_data.last_name

        if not email:
            email = db_data.email

        if not phone:
            phone = db_data.phone

        if not facebook:
            facebook = db_data.facebook

        if not instagram:
            instagram = db_data.instagram

        if not twitter:
            twitter = db_data.twitter

        if not linkedin:
            linkedin = db_data.linkedin

        if not state:
            state = db_data.state

        if avatar:
            valid_extension = ['jpg', 'gif', 'png',
                               'jpeg', 'svg', 'JPG', 'JPEG']
            avatar_url = serializer.data['avatar']
            # print("avatar", avatar, "url seriaili", avatar_url.name.split('.')[-1])
            if avatar_url.name.split('.')[-1] not in valid_extension:
                return Response({"error": "invalid file format"}, status=status.HTTP_400_BAD_REQUEST)

            upload_image = cloudinary.uploader.upload(avatar_url, folder=config(
                'FOLDER_NAME'), user_filename=True, overwrite=True)
            avatar = upload_image.get('url')
        else:
            avatar = db_data.avatar

        db_data.first_name = first_name
        db_data.last_name = last_name
        db_data.email = email
        db_data.phone = phone
        db_data.facebook = facebook
        db_data.twitter = twitter
        db_data.instagram = instagram
        db_data.linkedin = linkedin
        db_data.state = state
        db_data.avatar = avatar
        db_data.save()

        return Response({"message": "success"}, status=status.HTTP_200_OK)
