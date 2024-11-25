from django.shortcuts import render
from django.http import HttpResponse
from .models import PlantData
import json

# index.html 페이지를 부르는 index 함수
def index(request):
    datalist = PlantData.objects.all()
    return render(request, 'main/index.html', {"datalist": datalist})

def update(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))

        data = PlantData.objects.first()

        data.soil_moisture = body["plantSoilMoisture"]
        data.temperature = body["plantTemperature"]
        data.humidity = body["plantHumidity"]
        data.illuminance = body["plantIlluminance"]

        data.save()
        
        # init regacy
        # data = PlantData.objects.create(
        #     soil_moisture = 0,
        #     temperature = 0,
        #     humidity = 0,
        #     illuminance = 0,
        # )

        # return render(request, 'main/index.html', {'data': data})
        return HttpResponse(json.dumps(body))
    else:
        data = PlantData.objects.first().dict_data()
        return HttpResponse(json.dumps(data))