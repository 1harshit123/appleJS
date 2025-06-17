from django.db import models

# Create your models here.
class Apple(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    date = models.DateField()
