from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='measurement', on_delete=models.CASCADE, null=True, default=None)
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
