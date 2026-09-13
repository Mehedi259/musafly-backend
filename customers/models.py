from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    total_bookings = models.IntegerField(default=0)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
