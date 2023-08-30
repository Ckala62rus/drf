from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Raiting, RaitingStar, Review

# Register your models here.

# admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Raiting)
admin.site.register(RaitingStar)
admin.site.register(Review)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url', 'custom_field')
