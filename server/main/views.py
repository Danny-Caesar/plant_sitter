from django.shortcuts import render
from .models import PlantData

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

def update(request):
    data = PlantData.objects.create(
        soil_moisture = request.POST['soil_moisture'],
        illuminacne = request.POST['illuminance'],
        temperature = request.POST['temperature'],
        humidity = request.POST['humidity'],
    )
    return render(request, 'main/index.html', {'plantdata': data})