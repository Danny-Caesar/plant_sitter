from django.db import models

class PlantData(models.Model):
    soil_moisture = models.CharField(max_length=10)
    temperature = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    illuminance = models.CharField(max_length=10)