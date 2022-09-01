from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class CardeiUserManager(UserManager):
    def create_user(self, username='', email=None, password=None, **extra_fields):
        print
        return super().create_user(username=email, email=email, password=password,
                                   **extra_fields)


class CardeiUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
