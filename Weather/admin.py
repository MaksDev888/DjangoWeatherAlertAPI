from django.contrib import admin

from Weather.models import Weather


class WeatherAppAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created")
    fields = ("created", "feels_like", "pressure", "visibility", "wind", "city")
    readonly_fields = ("created", "feels_like", "pressure", "visibility", "wind", "city")
    list_filter = ("created",)


admin.site.register(Weather, WeatherAppAdmin)
