from django.db import models

class PlantData(models.Model):
    soil_moisture = models.CharField(max_length=10)
    temperature = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    illuminance = models.CharField(max_length=10)

    # def __init__(self, soil_moisture, temperature, humidity, illuminance):
    #     self.soil_moisture = soil_moisture
    #     self.temperature = temperature
    #     self.humidity = humidity
    #     self.illuminance = illuminance

    def dict_data(self):
        di = {"soil_moisture" : self.soil_moisture,
                "temperature" : self.temperature,
                "humidity" : self.humidity,
                "illuminance" : self.illuminance,}
        return di