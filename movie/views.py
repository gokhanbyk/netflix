from django.shortcuts import render
from user.models import *

# Create your views here.
def index_view(request):
    

    return render(request, 'movie/index.html', {})

def movies_view(request, profile_slug):
    
    profile = Profile.objects.get(slug = profile_slug)

    return render(request, 'movie/movies.html', {
        'profile': profile
    })