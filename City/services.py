from City.models import City
from Weather.models import Weather


def get_all_cities() -> list[City]:
    return City.objects.all()


def update_weather(result: dict, kwargs: dict) -> None:
    Weather.objects.filter(city_id=kwargs["pk"]).update(
        temp=result["main"]["temp"],
        feels_like=result["main"]["feels_like"],
        pressure=result["main"]["pressure"],
        visibility=result["visibility"],
        wind=result["wind"]["speed"],
    )


def create_weather(result: dict, kwargs: dict) -> None:
    Weather.objects.create(
        city_id=kwargs["pk"],
        temp=result["main"]["temp"],
        feels_like=result["main"]["feels_like"],
        pressure=result["main"]["pressure"],
        visibility=result["visibility"],
        wind=result["wind"]["speed"],
    )
