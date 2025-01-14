from django.shortcuts import render, HttpResponse
from . import models

def home(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')
        checkbox = request.POST.get('checkbox')

        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False

        student = models.Student(name=name, email=email, phone=phone, password=password, checkbox=checkbox, photo=photo)
        student.save()
        return render(request, 'student/index.html')

    return render(request, 'student/index.html')
