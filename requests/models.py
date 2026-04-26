from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Requests(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    pg_id = models.CharField(max_length=100, default='')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name