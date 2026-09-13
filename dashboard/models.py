from django.db import models
from django.utils import timezone

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('ফ্লাইট', 'ফ্লাইট'),
        ('হোটেল', 'হোটেল'),
        ('ট্যুর', 'ট্যুর'),
        ('ট্রান্সফার', 'ট্রান্সফার'),
    ]
    
    booking_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    booking_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, default='কনফার্মড')
    status_color = models.CharField(max_length=100, default='bg-green-100 text-green-700')

    def __str__(self):
        return f"{self.booking_id} - {self.customer_name}"

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    percent = models.IntegerField(default=0)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
