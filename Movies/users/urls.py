from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path('users/reg/', RegistrationView.as_view()),
]