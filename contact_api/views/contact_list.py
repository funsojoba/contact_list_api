from contact_api.models.contact import ContactModel
from rest_framework.generics import ListAPIView
# from contact_api.serializers.contact_serializer import ContactSerializer
from contact_api.serializers.contact_list_serializer import ContactListSerializer


class ListContact(ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactListSerializer
