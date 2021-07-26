from django.contrib import admin

from authenticate.models import User

from .models.email import EmailModel
from .models.contact import ContactModel

admin.site.register((User, ContactModel, EmailModel))
