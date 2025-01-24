from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def home(request):
    return JsonResponse({'message' : 'Site run successfully!!'})
