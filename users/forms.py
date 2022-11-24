from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile





class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=False) #no quiero que el mail sea obligatorio
    competicion1=forms.CharField()         #este es obligatorio, el usuario tiene que anotarse a una competencia al menos
    competicion2=forms.CharField(required=False) #este no es obligatorio, si se quiere anotar a dos competencias puede hacerlo, pero no es obligatorio 

    class Meta:
        model=User
        fields = ['username', 'email','competicion1','competicion2', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']