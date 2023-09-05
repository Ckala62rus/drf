from django.urls import path
from .views import RegistrationView, ChangePasswordView, MeView

urlpatterns = [
    path('users/reg/', RegistrationView.as_view(), name='reg'),
    path('users/me/', MeView.as_view(), name='me'),
    path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
