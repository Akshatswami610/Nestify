from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Requests(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'), ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    pg_id = models.CharField(max_length=100, default='')
    visit_date = models.DateField()
    visit_time = models.TimeField()
    status = models.CharField(choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name