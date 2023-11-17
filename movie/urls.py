from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('movies/<slug:profile_slug>/', movies_view, name="movies_page"),
    path('movie/<slug:movie_slug>/', movie_video_view, name="movie_video_page"),
    path('movies/<slug:profile_slug>/<slug:slug>/', movies_type_view, name="movies_type_page"),
    # path('movies/<slug:profile_slug>/search/', movies_search_view, name="movies_search_page"),
]
