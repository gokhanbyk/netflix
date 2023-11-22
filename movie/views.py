from django.shortcuts import render, redirect
from user.models import *
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
# ! Custom 404 Sayfası için
def Page_404(request, exception):

    return render(request, '404/404_Page.html', {})
# ! Custom 404 Sayfası için

def index_view(request):
    if request.user.is_authenticated:
        return redirect('profiles_page')
    return render(request, 'movie/index.html', {})


@login_required(login_url="/user/login/")
def movies_view(request, profile_slug):
    
    profile = Profile.objects.get(slug = profile_slug)
    movies = Movies.objects.all()
    categories = Category.objects.all()
    genres = Genre.objects.all()

    profiles = request.user.profile_set.all()

    # ! İzlenme Sırasına Göre film gösterme
    top_movies = Movies.objects.all().order_by('-view_count')

    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET.get('q')
        turler = Genre.objects.filter(name__contains = q)
        kategoriler = Category.objects.filter(name__contains = q)

        print(turler)

        filmler = Movies.objects.filter(name__contains = q) or Movies.objects.filter(genre__in = turler) or Movies.objects.filter(category__in = kategoriler)

        
        return render(request, 'movie/movies.html', {
            'categories': categories,
            'genres': genres,
            'profiles': profiles,
            'profile': profile,
            'filmler': filmler,
            'top_movies': top_movies
        })

    return render(request, 'movie/movies.html', {
        'profile': profile,
        'movies': movies,
        'categories': categories,
        'genres': genres,
        'profiles': profiles,
        'top_movies': top_movies
    })

@login_required(login_url="/user/login/")
def movie_video_view(request, movie_slug):

    movie = Movies.objects.get(slug = movie_slug)
    movie.view_count += 1
    movie.save()

    return render(request, 'movie/video.html', {
        'movie': movie
    })


def movies_type_view(request, profile_slug,slug):

    movies_category = Movies.objects.filter(category__slug = slug)
    movies_genre = Movies.objects.filter(genre__slug = slug)

    categories = Category.objects.all()
    genres = Genre.objects.all()

    profile = Profile.objects.get(slug = profile_slug)

    profiles = request.user.profile_set.all()

    return render(request, 'movie/movies.html', {
        'movies_category': movies_category,
        'movies_genre': movies_genre,
        'categories': categories,
        'genres': genres,
        'profiles': profiles,
        'profile': profile,
    })

# def movies_search_view(request, profile_slug):
#     categories = Category.objects.all()
#     genres = Genre.objects.all()
#     profile = Profile.objects.get(slug = profile_slug)
#     profiles = request.user.profile_set.all()

#     if 'q' in request.GET and request.GET.get('q'):
#         q = request.GET.get('q')
#         turler = Genre.objects.filter(name__contains = q)
#         kategoriler = Category.objects.filter(name__contains = q)

#         print(turler)

#         filmler = Movies.objects.filter(name__contains = q) or Movies.objects.filter(genre__in = turler) or Movies.objects.filter(category__in = kategoriler)

        
#         return render(request, 'movie/movies.html', {
#             'categories': categories,
#             'genres': genres,
#             'profiles': profiles,
#             'profile': profile,
#             'filmler': filmler
#         })
