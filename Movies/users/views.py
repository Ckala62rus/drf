from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import users as user_s

# Create your views here.

User = get_user_model()


@extend_schema_view(
    post=extend_schema(
        summary='Регистрация пользователя',
        tags=['Аутентификация & Авторизация']
    ),
)
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = user_s.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        summary='Сменя пароля',
        tags=['Аутентификация & Авторизация'],
        request=user_s.ChangePasswordSerializer
    ),
)
class ChangePasswordView(APIView):

    def post(self, request, password=None):
        user = request.user
        serializer = user_s.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse("test test test 123")


@extend_schema_view(
    get=extend_schema(
        summary='Профиль пользователя',
        tags=['Пользователи'],
    ),
    put=extend_schema(
        summary='Изменить профиль пользователя',
        tags=['Пользователи'],
    ),
    patch=extend_schema(
        summary='Изменить частично профиль пользователя',
        tags=['Пользователи'],
    ),
)
class MeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = user_s.MeSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return user_s.MeUpdateSerializer

        return  user_s.MeSerializer

    # this is required method for get_serializer_class
    def get_object(self):
        return self.request.user
