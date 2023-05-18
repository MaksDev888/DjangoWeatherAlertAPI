from django.db import models
from City.models import City


class Weather(models.Model):
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Created")
    temp = models.CharField(max_length=5, verbose_name="Temperature in °C", blank=True, null=True)
    feels_like = models.CharField(max_length=5, verbose_name="Feels like in °C", blank=True, null=True)
    pressure = models.CharField(max_length=5, verbose_name="Pressure", blank=True, null=True)
    visibility = models.CharField(max_length=20, verbose_name="Visibility", blank=True, null=True)
    wind = models.CharField(max_length=10, verbose_name="Wind metrs per second", blank=True, null=True)
    icon = models.CharField(max_length=200, verbose_name="Icon", blank=True, null=True)
    city = models.ForeignKey(City, related_name="weather", on_delete=models.CASCADE, verbose_name="City", null=True)

    class Meta:
        verbose_name = "Weather"
        verbose_name_plural = "Weather"
        ordering = ["-created"]

    def __str__(self):
        return f"Temp: {self.temp} in the {self.city}"
