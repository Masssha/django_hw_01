from django.db import models

class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    measurements = models.ManyToManyField(Measurement)

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
