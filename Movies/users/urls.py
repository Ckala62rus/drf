from django.urls import path
from .views import RegistrationView, ChangePasswordView

urlpatterns = [
    path('users/reg/', RegistrationView.as_view(), name='reg'),
    path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
