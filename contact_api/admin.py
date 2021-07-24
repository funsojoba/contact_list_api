from django.contrib import admin
from .models.contact import ContactModel
from authenticate.models import User


admin.site.register((User, ContactModel))
