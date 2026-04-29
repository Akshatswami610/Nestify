from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Support(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name