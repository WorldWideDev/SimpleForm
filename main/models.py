from django.db import models

# Create your models here.
class Sample(models.Model):
    favorite_food = models.CharField(max_length=5)
    favorite_color = models.CharField(max_length=5)