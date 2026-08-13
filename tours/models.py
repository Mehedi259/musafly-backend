from django.db import models

class Tour(models.Model):
    destination = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inclusions = models.TextField()
    image = models.ImageField(upload_to="tours/", blank=True, null=True)

    def __str__(self):
        return f"{self.destination} - {self.duration}"
