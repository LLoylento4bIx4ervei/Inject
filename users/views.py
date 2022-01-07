from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):

        form = UserCreationForm(request.POST)
        return render(request, 'users/register.html', {'form':form})

