from rest_framework import serializers

from City.models import City
from Weather.serializers import WeatherAppSerializers


class CitiesSerializer(serializers.ModelSerializer):
    weather = WeatherAppSerializers(many=True)

    class Meta:
        model = City
        fields = ["name", "weather"]


class CreateCitySerializer(serializers.ModelSerializer):
    weather = WeatherAppSerializers(many=True)

    class Meta:
        model = City
        fields = ["name", "weather"]
