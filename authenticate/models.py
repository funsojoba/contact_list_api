import uuid
from django.db import models

from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations=True

    def _create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError("email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        password = user.set_password(password)
        user.save(using=self._db)
    
    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extrafields)
    
    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_staff', True)
        return self._create_user(email=email, password=password, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):
    AVATAR_URL = 'https://res.cloudinary.com/ddl2pf4qh/image/upload/v1627605865/contact_api/avatar3_chs26r.png'
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    avatar = models.URLField(default=AVATAR_URL)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email
