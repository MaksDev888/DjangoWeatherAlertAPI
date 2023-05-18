from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from FollowList.models import FollowList
from FollowList.serializers import FollowListSerializers, FollowlistAddSerializer


class FollowAPIListView(viewsets.GenericViewSet):
    queryset = FollowList.objects.all()
    serializer_class = FollowListSerializers
    permission_class = [
        IsAuthenticated,
    ]

    def list(self, request: Request) -> Response:
        serializer = FollowListSerializers(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: str = None) -> Response:
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer = FollowListSerializers(queryset)
        return Response(serializer.data)


class FollowUserApiView(generics.ListCreateAPIView):
    serializer_class = FollowListSerializers
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self) -> list:
        return FollowList.objects.filter(user_id=self.request.user)


class FollowListAddView(generics.CreateAPIView):
    queryset = FollowList.objects.all()
    serializer_class = FollowlistAddSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class FollowListDeleteView(generics.DestroyAPIView):
    queryset = FollowList.objects.all()
    serializer_class = FollowListSerializers
    permission_classes = [
        IsAuthenticated,
    ]
