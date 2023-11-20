from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *

class UserLoginForm(forms.Form):
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Giriniz'}))

   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre Giriniz'}))

   def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            self.add_error('email', 'Bu email mevcut değil!')

        return email


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'name',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'form-control'})
        self.fields['name'].widget = widgets.TextInput(attrs={'class': 'form-control'})


class ChangeUserPassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password Confirmation'})