from django.db import models

class UmrahPackage(models.Model):
    package_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inclusions = models.TextField()
    image = models.ImageField(upload_to="umrah/", blank=True, null=True)

    def __str__(self):
        return self.package_name
