from django.urls import path
from .views.contact_view import Contact


urlpatterns = [
    path('', Contact.as_view(), name="contact")
]
