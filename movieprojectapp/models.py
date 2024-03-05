# models.py
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    year = models.DateField()
    image = models.ImageField(upload_to='movieimages')
    is_coming_soon = models.BooleanField(default=False)  # Add a field for coming soon
    is_running = models.BooleanField(default=False)
    is_international_release = models.BooleanField(default=False)


    def __str__(self):
        return self.name

