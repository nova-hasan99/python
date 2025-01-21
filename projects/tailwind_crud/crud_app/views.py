from django.shortcuts import render

def home(request):
    return render(request, 'studentData.html')

def form(request):
    return render(request, 'studentForm.html')

