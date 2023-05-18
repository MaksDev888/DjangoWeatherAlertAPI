import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from DjangoWeatherAlert import settings

from City.models import City
from City.services import get_all_cities, update_weather, create_weather
from City.serializers import CitiesSerializer, CreateCitySerializer
from Weather.models import Weather


class CityListAPIView(generics.ListCreateAPIView):
    queryset = get_all_cities()
    serializer_class = CitiesSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request: Request, *args, **kwargs: dict) -> Response:
        serializer = CreateCitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = get_all_cities()
    serializer_class = CitiesSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request: Request, *args, **kwargs: dict) -> Response:
        url = settings.WEATHER_URL + settings.WEATHER_API_KEY
        city = City.objects.filter(pk=self.kwargs["pk"])
        if city:
            response = requests.get(url.format(city[0].name)).json()
            if Weather.objects.filter(city_id=city[0].id).exists():
                update_weather(response, self.kwargs)
            else:
                create_weather(response, self.kwargs)
            return Response(response)
        else:
            return Response("Города не существует, проверьть верность запроса", status=404)
