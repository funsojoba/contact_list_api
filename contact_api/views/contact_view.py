from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from contact_api.serializers.contact_serializer import ContactModel, ContactSerializer


class Contact(APIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        return Response({"message": "welcome home amigos"})
