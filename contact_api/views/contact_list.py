from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from contact_api.models.contact import ContactModel
from contact_api.serializers.contact_list_serializer import ContactListSerializer
from contact_api.serializers.contact_serializer import ContactSerializer

class ListContact(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactListSerializer

    def get(self, request):
        queryset = ContactModel.objects.all()
        serializer = ContactListSerializer(queryset, many=True)
        data = serializer.data
        count = queryset.count()

        return Response({"data":data, "count":count, "message":"success"}, status=status.HTTP_200_OK)
