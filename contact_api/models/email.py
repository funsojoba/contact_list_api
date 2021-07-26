from django.db import models
import uuid
from authenticate.models import User


class EmailModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    reciever = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Email from {self.sender.first_name} to {self.reciever}'
