from django.contrib import admin
from django.utils.safestring import mark_safe

from .models.post import Post
from .models.post_file import PostFile


# Register your models here.


# admin.site.register(Post)

class PostFileInlines(admin.StackedInline):
    model = PostFile
    fields = ('id', 'file', 'description',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", 'is_publish')
    list_display_links = ('id', 'title',)
    readonly_fields = ('created_at', 'updated_at',)
    list_editable = ('is_publish',)
    filter = ('is_publish', )
    save_on_top = True
    inlines = [PostFileInlines]


@admin.register(PostFile)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'description', 'image_tag')
    readonly_fields = ('image_tag',)
