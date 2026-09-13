from django.db import models

class Deal(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    passport_number = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    service_category = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    lead_source = models.CharField(max_length=100)
    deal_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service_category}"
