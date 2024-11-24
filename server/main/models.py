from django.db import models

class PlantData(models.Model):
    soil_moisture = models.TextField()
    illuminance = models.TextField()
    humidity = models.TextField()
    temperature = models.TextField()