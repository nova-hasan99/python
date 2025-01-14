from django.urls import path
from hotel.views import add_hotel, all_hotels, update_hotel, delete_hotel

urlpatterns = [
    path('', all_hotels, name = 'allhotels'),
    path('add_hotel/', add_hotel, name = 'addhotel'),
    path('update_hotel/<int:id>', update_hotel, name = 'updatehotel'),
    path('delete_hotel/<int:id>', delete_hotel, name = 'deletehotel')
]
