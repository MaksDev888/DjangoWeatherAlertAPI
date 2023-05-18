from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from User.views import RegisterApiView, UserAPIView

app_name = "User"

urlpatterns = [
    path("api/v1/register/", RegisterApiView.as_view(), name="register"),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

router = routers.DefaultRouter()
router.register(r"users", UserAPIView)

urlpatterns += router.urls
