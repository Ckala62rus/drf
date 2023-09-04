from django.urls import path, include

from .spectacular.urls import urlpatterns as doc_urls
# from Movies.users.urls import urlpatterns as user_urls
from users.urls import urlpatterns as user_urls # it's work with docker!

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
