from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_image']

    class CustomAuthenticationForm(AuthenticationForm):
        username = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
        )
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        )
