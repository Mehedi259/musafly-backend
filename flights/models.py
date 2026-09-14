from django.db import models

class Flight(models.Model):
    airline = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="flights/", blank=True, null=True)

    def __str__(self):
        return f"{self.airline}: {self.origin} to {self.destination}"
