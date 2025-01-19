from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def data(request):
    # return JsonResponse({'message' : 'welcome to templates'})
    parson = {'first_name' : 'Rahhim', 'last_name' : 'Uddin', 'age' : 24}
    return render(request, 'data.html', {'name' : parson})

def loop(request):
    data = [('Rahim', 24), ('Karim', 22), ('Barkat', 25), ('Jabbar', 20), ('Rahik', 30)]
    tempareture = 26
    return render(request, 'loop.html', {'parsons' : data, 'temp': tempareture})


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def reports(request):
    return render(request, 'reports.html')
