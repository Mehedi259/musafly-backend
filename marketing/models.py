from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    spent = models.CharField(max_length=100)
    reach = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
