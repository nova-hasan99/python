from django.shortcuts import render, redirect
from hotel.models import HotelStoreModel
from hotel.forms import HotelStoreModelForm

def add_hotel(request):
    if request.method == 'POST':
        hotel = HotelStoreModelForm(request.POST)
        if hotel.is_valid():
            hotel.save()
            return redirect('#')
    else:
        hotel = HotelStoreModelForm()
    return render(request, '#', {'form':hotel})

def all_hotels(request):
    hotel = HotelStoreModel.objects.all()
    return render(request, '#', {'data':hotel})

def update_hotel(request, id):
    hotel = HotelStoreModel.objects.get(pk=id)
    form = HotelStoreModelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelStoreModelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        return render(request, '#', {form:form})
    
def delete_hotel(request, id):
    hotel = HotelStoreModelForm.objects.get(pk=id).delete()
    return redirect('#')
