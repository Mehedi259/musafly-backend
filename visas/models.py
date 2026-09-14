from django.db import models

class Visa(models.Model):
    country = models.CharField(max_length=255)
    visa_type = models.CharField(max_length=255)
    processing_time = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requirements = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="visas/", blank=True, null=True)

    def __str__(self):
        return f"{self.country} - {self.visa_type}"
