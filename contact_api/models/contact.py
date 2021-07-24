from django.db import models


class ContactModel(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.URLField(
        default="https://res.cloudinary.com/ddl2pf4qh/image/upload/v1623512852/24-248253_user-profile-default-image-png-clipart-png-download_qwj0qi.png")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
