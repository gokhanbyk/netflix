from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('movies/<slug:profile_slug>/', movies_view, name="movies_page"),
    path('movie/<slug:movie_slug>/', movie_video_view, name="movie_video_page"),
    
]
