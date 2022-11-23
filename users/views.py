from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method =='POST':
        form = UserCreationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.succes(request, f'Usuario {username} creado con exito!')
            return redirect ('blog-home')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'users/register.html',{'form':form})













# Create your views here.
