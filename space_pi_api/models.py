from django.db import models

# Create your models here.

class TempHistory(models.Model):
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True)
    sensor = models.IntegerField()

class HumidityHistory(models.Model):
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True)
    sensor = models.IntegerField()

