import requests
from DjangoWeatherAlert import settings
from DjangoWeatherAlert.celery import app
from .models import City
from .services import update_weather


URL = settings.WEATHER_URL + settings.WEATHER_API_KEY


@app.task(name="Constant updates")
def constant_weather_update_every_one_hour() -> str:
    cities = City.objects.all()
    if not cities:
        return "Cities not found"
    for city in cities:
        result = requests.get(URL.format(city.name)).json()

        update_weather(result, {"pk": city.pk})
    return "Successfully"
