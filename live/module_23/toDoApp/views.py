from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import UserRegistrationForm

def home(request):
    return render(request, "todoapp/login.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('login')
    form = UserRegistrationForm()
    return render(request, 'todoapp/register.html', {'form' : form})
