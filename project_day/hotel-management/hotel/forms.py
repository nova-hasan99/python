from django import forms
from hotel.models import HotelStoreModel

class HotelStoreModelForm(forms.ModelForm):
    class Meta:
        model = HotelStoreModel
        fields = ['id', 'hotel_name', 'owner_name']