from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics

from .models import Movie, Genre, Category
from .serializers import CategorySerializer, CategoryListSerializer


# Create your views here.

class MovieView(View):
    """Список фильмов"""

    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movies_list": movie})

    def test(self, id: int):
        return HttpResponse(f'Find model by id:{id}')


class CategoryCreateViewApi(generics.CreateAPIView):
    """Category create"""
    queryset = Category.objects.all()
    # serializer = CategorySerializer()
    # serializer.is_valid(raise_exception=True)
    serializer_class = CategorySerializer


class CategoryListViewApi(generics.ListAPIView):
    """Category all"""
    queryset = Category.objects.all()
    # test = list(Category.objects.all().values())
    serializer_class = CategoryListSerializer
