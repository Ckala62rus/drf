from django.urls import path

from posts.views import (
    PostsView,
    PostsDeleteView,
    PostsUpdateView,
)

urlpatterns = [
    # path('v1/posts/', GetPosts, name='all'),
    path('v1/posts/', PostsView.as_view(), name='all-posts'),
    path('v1/posts/<int:id>/', PostsDeleteView.as_view(), name='delete-post'),
    path('v1/posts/update/<int:id>/', PostsUpdateView.as_view(), name='update-post'),
]
