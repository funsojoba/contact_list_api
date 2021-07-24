from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from contact_api.models.contact import ContactModel
from contact_api.serializers.contact_list_serializer import ContactListSerializer


class UpdateContactView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ContactModel.objects.all()
    serializer_class = ContactListSerializer
