from django.db import models

class Transaction(models.Model):
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class MonthlyStat(models.Model):
    month = models.CharField(max_length=50)
    revenue = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)

    def __str__(self):
        return self.month
