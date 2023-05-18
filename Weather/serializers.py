from rest_framework import serializers

from Weather.models import Weather


class WeatherAppSerializers(serializers.ModelSerializer):
    def get_fields(self) -> dict:
        fields = super().get_fields()
        for field in fields.values():
            field.read_only = True
        return fields

    class Meta:
        model = Weather
        fields = "__all__"
