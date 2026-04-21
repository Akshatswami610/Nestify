from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email