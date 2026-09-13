from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    price = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
