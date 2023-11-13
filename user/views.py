from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, authenticate, logout
from .models import *

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('profiles_page')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = User.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('profiles_page')
            else:
                return render(request, 'user/login.html', {
                    'form': form
                })
        else:
            return render(request, 'user/login.html', {
                    'form': form
                })
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {
            'form': form
        })
    

def register_view(request):

    if request.user.is_authenticated:
        return redirect('profiles_page')

    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('profiles_page')
        else:
            form = Register()
            return render(request, 'user/register.html', {
                'form': form
            })

    form = Register()
    return render(request, 'user/register.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('index_page')

def profiles_view(request):

    profiles = Profile.objects.filter(owner = request.user)

    
    return render(request, 'user/profiles.html', {
        'profiles': profiles
    })

def profile_add_view(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            return redirect('profiles_page')
        else:
            return render(request, 'user/profiles.html', {
                'form': form
            })

    form = UserProfileForm()
    return render(request, 'user/profiles.html', {
        'form': form
    })

def profile_manage_view(request):

    profiles = Profile.objects.filter(owner = request.user)
    

    return render(request, 'user/profile-manage.html', {
        'profiles': profiles
    })

def profile_edit_view(request, profile_slug): 
    
    profile = Profile.objects.get(slug = profile_slug)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            return redirect('profiles_page')
        else:
            return render(request, 'user/profile-edit.html', {
                'form': form,
                'profile': profile
            })

    form = UserProfileForm(instance=profile)
    return render(request, 'user/profile-edit.html', {
        'form': form,
        'profile': profile
    })


def profile_delete_view(request, profile_slug):

    profile = Profile.objects.get(slug = profile_slug)

    if request.method == 'POST':
        profile.delete()
        return redirect('profiles_page')
    else:
        return render(request, 'user/delete.html', {
            'profile': profile
        })