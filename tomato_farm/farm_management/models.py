from django.db import models
from django.utils import timezone


class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Crop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop_type = models.CharField(max_length=50)
    planted_at = models.DateTimeField()
    harvest_estimate = models.DateTimeField()

    def __str__(self):
        return f"{self.crop_type} at {self.farm.name}"


class Sensor(models.Model):
    SENSOR_TYPES = (
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('ph', 'pH')
    )

    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.sensor_type}) at {self.farm.name}"


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    value = models.FloatField()

    def __str__(self):
        return f"{self.sensor.sensor_type} reading at {self.timestamp}"
