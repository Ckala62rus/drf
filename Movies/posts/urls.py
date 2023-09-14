from django.urls import path

from posts.views import PostsView, PostsDeleteView

urlpatterns = [
    # path('v1/posts/', GetPosts, name='all'),
    path('v1/posts/', PostsView.as_view(), name='all-posts'),
    path('v1/posts/<int:id>/', PostsDeleteView.as_view(), name='delete-post')
]