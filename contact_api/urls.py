from django.urls import path
from .views.contact_view import Contact
from .views.contact_list import ListContact
from .views.update_contact import UpdateContactView
from .views.send_mail import SendMail


urlpatterns = [
    path('', ListContact.as_view(), name="contacts"),
    path('create-contact', Contact.as_view(), name="create-contact"),
    path('update-contact/<str:pk>',
         UpdateContactView.as_view(), name="update-contact"),
    path('send-mail/<str:pk>', SendMail.as_view(), name='send-mail')
]
