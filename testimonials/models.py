from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    rating = models.IntegerField(default=5)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
