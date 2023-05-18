from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from User.models import UserApp
from .serializers import (
    UserSerializer,
    UsersSerializer,
    RegisterSerializer,
    UpdateUserSerializer,
    PasswordChangeSerializer,
)
from .services import get_all_users


class UserAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = get_all_users()
    serializer_class = UserSerializer

    def get_serializer_class(self) -> type:
        if self.action in ["me", "retrieve"]:
            return UserSerializer
        elif self.action == "list":
            return UsersSerializer
        elif self.action == "update":
            return UpdateUserSerializer
        elif self.action == "password_change":
            return PasswordChangeSerializer

    def list(self, request: list) -> Response:
        serializer = UsersSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: list, pk: str = None) -> Response:
        user = get_object_or_404(UserApp, pk=pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def update(self, request: list, pk: str) -> Response:
        user = request.user
        serializer = self.get_serializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("username", None)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_205_RESET_CONTENT)

    @action(detail=False, methods=["get"])
    def me(self, request: list) -> Response:
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def change_password(self, request: list, pk: str) -> Response:
        user = request.user
        serializer = PasswordChangeSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Пароль успешно изменен", status=status.HTTP_205_RESET_CONTENT)


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = get_all_users()
    permission_classes = (AllowAny,)

    def post(self, request: list, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            },
        )
