from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return HttpResponse('This is Student Home page')

def profile(request):
    context = {
        'name': 'John Doe',
        'age': 18,
        'major': 'Computer Science'
    }
    marks = [
        {
            'id' : 1,
            'subject' : 'Math',
            'marks' : 90
        },
        {
            'id' : 2,
            'subject' : 'English',
            'marks' : 75
        },
        {
            'id' : 3,
            'subject' : 'Science',
            'marks' : 95
        },
        {
            'id' : 4,
            'subject' : 'History',
            'marks' : 40
        }
    ]
    student_data = models.Student.objects.all()
    return render(request, 'student/index.html', {'marks': marks, 'context' : context, 'student_data' : student_data})


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return HttpResponse('Student deleted successfully')






