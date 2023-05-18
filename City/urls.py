from django.urls import path

from City.views import CityListAPIView, CityDetailAPIView

app_name = "City"

urlpatterns = [
    path("city/", CityListAPIView.as_view(), name="city_list"),
    path("city/<int:pk>/", CityDetailAPIView.as_view(), name="city_detail"),
]
