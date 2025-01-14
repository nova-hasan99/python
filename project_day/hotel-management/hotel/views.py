from django.shortcuts import render, redirect, HttpResponse
from hotel.models import HotelStoreModel
from hotel.forms import HotelStoreModelForm

def add_hotel(request):
    if request.method == 'POST':
        hotel = HotelStoreModelForm(request.POST)
        if hotel.is_valid():
            hotel.save()
            return redirect('allhotels')
    else:
        hotel = HotelStoreModelForm()
    return render(request, 'add_hotel.html', {'form':hotel})
    

def all_hotels(request):
    hotel = HotelStoreModel.objects.all()
    return render(request, 'all_hotels.html', {'data':hotel})
    # return HttpResponse("hi")

def update_hotel(request, id):
    hotel = HotelStoreModel.objects.get(pk=id)
    form = HotelStoreModelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelStoreModelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('allhotels')
    else:
        return render(request, 'add_hotel.html', {form:form})
    
def delete_hotel(request, id):
    hotel = HotelStoreModelForm.objects.get(pk=id).delete()
    return redirect('#')
