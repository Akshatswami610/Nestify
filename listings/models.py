from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class PG(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pgs'
    )

    name = models.CharField(max_length=200)
    description = models.TextField()

    rent = models.IntegerField()
    deposit = models.IntegerField(blank=True, null=True)
    booking_fees = models.IntegerField(blank=True, null=True)

    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    # Facilities
    wifi = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    # Gender preference
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('any', 'Any'),
    )
    gender_preference = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='any'
    )

    # Availability
    is_available = models.BooleanField(default=True)


    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PGImage(models.Model):
    pg = models.ForeignKey(PG, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pg_images/')