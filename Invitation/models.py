from django.db import models
from django.utils import timezone

# Create your models here.
class Wishe(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    relationship=models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.author