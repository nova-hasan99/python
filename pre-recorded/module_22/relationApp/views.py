from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.db.models import Prefetch


def home(request):
    car_models = models.CarModel.objects.select_related('car_company__ceo').prefetch_related(Prefetch('fueltype_set'))
    car_details = []
    for car in car_models:
        car_details.append({
            'car_name' : car.name,
            'car_company' : car.car_company.name,
            'ceo_name' : car.car_company.ceo.name,
            'fuel_names' : [fuel.name for fuel in models.FuelType.objects.filter(car_models = car)]

        })
    return render(request, 'cars/home.html', {'car_details': car_details})
