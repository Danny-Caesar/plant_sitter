from django.shortcuts import render
from .models import PlantData
import json

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

def update(request):
    body = json.loads(request.body.decode('utf-8'))
    data = PlantData.objects.create(
        soil_moisture = body["plantSoilMoisture"],
        temperature = body["plantTemperature"],
        humidity = body["plantHumidity"],
        illuminance = body["plantIlluminance"],
    )
    # return render(request, 'main/index.html', {'data': data})
    return "success: " + body