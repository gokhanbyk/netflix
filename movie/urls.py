from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('movies/<slug:profile_slug>/', movies_view, name="movies_page")
]
