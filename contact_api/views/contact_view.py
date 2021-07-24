from rest_framework.views import APIView
from rest_framework.response import Response

from contact_api.serializers.contact_serializer import ContactModel, ContactSerializer


class Contact(APIView):
    serializer_class = ContactSerializer

    def post(self, request):
        return Response({"message": "welcome home amigos"})
