from django.urls import path

from . import views
from .views import CategoryCreateViewApi, CategoryListViewApi, MovieView

urlpatterns = [
    path("", views.MovieView.as_view()),
    path("test/<int:id>", MovieView.test, name='test'),
    path("categories/create", CategoryCreateViewApi.as_view()),
    path("categories/", CategoryListViewApi.as_view()),
]
