from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from contact_api.models.contact import ContactModel
from contact_api.serializers.update_contact_serializer import UpdateContactSerailzer
from decouple import config
import cloudinary.uploader


class UpdateContactView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ContactModel.objects.all()
    serializer_class = UpdateContactSerailzer

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

        db_data = ContactModel.objects.get(id=pk)
        serializer = UpdateContactSerailzer(data=data)
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

        db_data.first_name = first_name
        db_data.last_name = last_name
        db_data.email = email
        db_data.phone = phone
        db_data.facebook = facebook
        db_data.twitter = twitter
        db_data.instagram = instagram
        db_data.linkedin = linkedin
        db_data.state = state
        db_data.save()

        return Response({"message": "success"}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        db_data = ContactModel.objects.get(id=pk)
        db_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)