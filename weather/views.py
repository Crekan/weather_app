import requests
from django.shortcuts import render

from weather.models import City
from .forms import CityForms


def index(request):
    appid = '08f2a575dda978b9c539199e54df03b0'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForms(request.POST)
        if form.is_valid():
            form.save()

    form = CityForms()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }

    return render(request, 'weather/index.html', context)
