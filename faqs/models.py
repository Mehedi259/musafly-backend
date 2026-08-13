from django.db import models

class FAQ(models.Model):
    CATEGORY_CHOICES = (
        ('general', 'General'),
        ('visa', 'Visa'),
        ('tours', 'Tours'),
        ('flights', 'Flights'),
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return self.question
