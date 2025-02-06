from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "todoapp/index.html")

def registration(request):
    return render(request, 'todoapp/registration.html')
