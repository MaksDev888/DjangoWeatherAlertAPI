from rest_framework import serializers

from User.models import UserApp


class UserSerializersSubscription(serializers.ModelSerializer):
    subscriptions = serializers.IntegerField(source="subscriptions_user.count", read_only=True)

    class Meta:
        model = UserApp
        fields = ("id", "username", "email", "first_name", "last_name", "bio", "subscriptions")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ("id", "username", "email", "first_name", "last_name", "bio", "is_verified", "is_staff")


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ("id", "username", "email", "first_name", "last_name", "bio")


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> UserApp:
        user = UserApp(**validated_data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = UserApp
        fields = ("id", "username", "password", "email", "first_name", "last_name", "bio")
        extra_kwargs = {"password": {"write_only": True}}


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Серелизатор для полного или частичного обновления модели.
    """

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = UserApp
        fields = ("first_name", "last_name", "bio", "password")
        extra_kwargs = {"password": {"write_only": True}}


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def update(self, instance: UserApp, validated_data: dict) -> UserApp:
        if instance.check_password(validated_data["old_password"]):
            instance.set_password(validated_data["password"])
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Неверный старый пароль")
