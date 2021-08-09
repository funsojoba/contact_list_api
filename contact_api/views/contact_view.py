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

        serializer = self.serializer_class(data=data)

        serializer.is_valid()

        contact = ContactModel.objects.create(
            owner=user,
            first_name=first_name, last_name=last_name, email=email, facebook=facebook,
            phone=phone, twitter=twitter, instagram=instagram, linkedin=linkedin, state=state)
        contact.save()

        serializer_dict = dict(serializer.data)

        return Response({"message":"success" ,"data":serializer_dict}, status=status.HTTP_201_CREATED)
