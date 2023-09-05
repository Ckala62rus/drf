from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
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

