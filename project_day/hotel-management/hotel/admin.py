from django.contrib import admin
from hotel.models import HotelStoreModel

class HotelStoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel_name', 'owner_name']

admin.site.register(HotelStoreModel, HotelStoreAdmin)
