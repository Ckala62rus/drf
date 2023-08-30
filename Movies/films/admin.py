from django.contrib import admin

from .models.actor import Actor
from .models.category import Category
from .models.genre import Genre
from .models.movie_shots import MovieShots
from .models.rating import Raiting
from .models.rating_star import RaitingStar
from .models.review import Review
from .models.movie import Movie

# Register your models here.

admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Raiting)
admin.site.register(RaitingStar)
admin.site.register(Review)
# admin.site.register(Movie)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url', 'custom_field')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def custom_field(self, obj):
        return f"{obj.id} ==> {obj.name} (поле которого нет в бд)"

    custom_field.short_description = 'Кастомное поле'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    autocomplete_fields = ('category',)
    save_on_top = True
