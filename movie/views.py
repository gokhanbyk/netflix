from django.shortcuts import render, redirect
from user.models import *
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
        return redirect('profiles_page')
    return render(request, 'movie/index.html', {})


@login_required(login_url="/user/login/")
def movies_view(request, profile_slug):
    
    profile = Profile.objects.get(slug = profile_slug)
    movies = Movies.objects.all()

    return render(request, 'movie/movies.html', {
        'profile': profile,
        'movies': movies,
    })