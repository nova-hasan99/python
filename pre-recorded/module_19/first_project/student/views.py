from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('This is Home page')

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
    return render(request, 'student/index.html', {'marks': marks})
