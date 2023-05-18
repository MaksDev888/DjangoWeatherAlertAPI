from django.urls import include, path
from rest_framework import routers

from FollowList.views import FollowAPIListView, FollowUserApiView, FollowListAddView, FollowListDeleteView

app_name = "FollowList"

router = routers.DefaultRouter()
router.register(r"follow", FollowAPIListView)

urlpatterns = [
    path("follow/follow_user_list/", FollowUserApiView.as_view(), name="follow_user_list"),
    path("follow/add_follow/", FollowListAddView.as_view(), name="add_follow"),
    path("follow/delete_follow/<int:pk>/", FollowListDeleteView.as_view(), name="delete_follow"),
    path("", include(router.urls)),
]
