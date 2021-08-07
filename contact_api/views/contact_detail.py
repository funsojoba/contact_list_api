from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from contact_api.serializers.contact_list_serializer import ContactListSerializer
from contact_api.models.contact import ContactModel



class ContactDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serialializer_class = ContactListSerializer
    

    def get(self, request, pk):
        queryset = ContactModel.objects.get(id=pk)
        serializer = ContactListSerializer(queryset)
        data = serializer.data

        return Response({"message":"success", "data":data}, status=status.HTTP_200_OK)