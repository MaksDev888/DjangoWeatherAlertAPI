import json

import pytest
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from City.models import City
from City.serializers import CitiesSerializer
from FollowList.models import FollowList
from FollowList.serializers import FollowListSerializers
from User.models import UserApp
from User.serializers import UsersSerializer, UserSerializer

list_urls = {
    "User: userapp_list",
    "User: userapp_me",
    "City: city_list",
    "FollowList: followlist-list",
    "FollowList: follow_user_list",
    "FollowList: add_follow",
}

list_pk_urls = {
    "User: userapp-change-password",
    "User: userapp-detail",
    "City: city_detail",
    "FollowList: followlist-detail",
}


class UserTests(APITestCase):
    def setUp(self) -> None:
        self.user = UserApp.objects.create_user(
            username="testuser",
            email="t@t.t",
            password="12345",
        )
        self.user2 = UserApp.objects.create_user(
            username="testuser2",
            email="t2@t.t",
            password="123456",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    @pytest.mark.django_db()
    def test_get_list_user(self) -> None:
        url = reverse("User:userapp-list")
        response = self.client.get(url)
        users = UserApp.objects.all()
        serializer = UsersSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db()
    def test_get_update_user(self) -> None:
        url = reverse("User:userapp-detail", kwargs={"pk": self.user2.id})
        response = self.client.get(url)
        user = UserApp.objects.get(id=self.user2.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

        url = reverse("User:userapp-detail", kwargs={"pk": self.user.id})
        response = self.client.put(url, data={"first_name": "change_name"})
        self.assertEqual("change_name", self.user.first_name)
        self.assertEqual(response.status_code, 205)

    @pytest.mark.django_db()
    def test_change_password(self) -> None:
        url = reverse("User:userapp-change-password", kwargs={"pk": self.user.id})
        self.client.post(url, data={"old_password": "12345", "password": "qwerty"})
        self.assertEqual(self.user.check_password("qwerty"), True)

    @pytest.mark.django_db()
    def test_user_me(self) -> None:
        url = reverse("User:userapp-me")
        response = self.client.get(url)
        user = UserApp.objects.get(id=self.user.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)


class CityTests(APITestCase):
    def setUp(self) -> None:
        self.user = UserApp.objects.create_user(
            username="testuser",
            email="t@t.t",
            password="12345",
        )
        self.city1 = City.objects.create(
            name="Moscow",
        )
        self.city2 = City.objects.create(
            name="city2",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    @pytest.mark.django_db()
    def test_get_list_city(self) -> None:
        url = reverse("City:city_list")
        response = self.client.get(url)
        cities = City.objects.all()
        serializer = CitiesSerializer(cities, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db()
    def test_get_weather_city(self) -> None:
        url = reverse("City:city_detail", kwargs={"pk": self.city1.id})
        response = self.client.get(url)
        self.assertEqual(response.data["sys"]["country"], "RU")
        self.assertEqual(response.status_code, 200)


class FollowListTests(APITestCase):
    def setUp(self) -> None:
        self.user = UserApp.objects.create(
            username="testuser",
            email="t@t.t",
            password="12345",
        )
        self.user2 = UserApp.objects.create(
            username="testuser2",
            email="t2@t.t",
            password="123456",
        )
        self.city1 = City.objects.create(
            name="Moscow",
        )
        self.city2 = City.objects.create(
            name="London",
        )
        self.follow1 = FollowList.objects.create(
            user_id=self.user,
            city_id=self.city1,
            send_time_email=3,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    @pytest.mark.django_db()
    def test_create_get_list_follow(self) -> None:
        url = reverse("FollowList:add_follow")
        data = {
            "city_id":self.city2.id,
            "send_time_email":3,
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type="application/json")
        self.assertEqual(response.data, {"city_id":self.city2.id,"send_time_email":3})

        url = reverse("FollowList:followlist-list")
        response = self.client.get(url)
        followlist = FollowList.objects.all()
        serialzier = FollowListSerializers(followlist, many=True)
        self.assertEqual(response.data, serialzier.data)
        self.assertEqual(response.status_code, 200)


        url = reverse("FollowList:follow_user_list")
        response = self.client.get(url)
        followlist = FollowList.objects.filter(user_id=self.user.id)
        serialzier = FollowListSerializers(followlist, many=True)
        self.assertEqual(response.data, serialzier.data)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db()
    def test_follow_list_detail(self) -> None:
        url = reverse("FollowList:followlist-detail", kwargs={"pk": self.follow1.id})
        response = self.client.get(url)
        followlist = FollowList.objects.get(id=self.follow1.id)
        serialzier = FollowListSerializers(followlist)
        self.assertEqual(response.data, serialzier.data)
        self.assertEqual(response.status_code, 200)


