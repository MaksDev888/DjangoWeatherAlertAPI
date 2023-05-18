from rest_framework import serializers

from User.models import UserApp
from City.serializers import CitiesSerializer
from FollowList.models import FollowList
from User.serializers import UserSerializersSubscription


class FollowListSerializers(serializers.ModelSerializer):
    user_id = UserSerializersSubscription()
    city_id = CitiesSerializer()

    class Meta:
        model = FollowList
        fields = ["user_id", "city_id", "send_time_email"]


class FollowlistAddSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data: dict) -> FollowList:
        user = UserApp.objects.get(email=validated_data.get("user_id"))
        if user.email:
            instance = FollowList.objects.create(**validated_data)
            return instance
        else:
            raise serializers.ValidationError('"Эмайл пользователя не найден"')

    class Meta:
        model = FollowList
        fields = ("user_id", "city_id", "send_time_email")
