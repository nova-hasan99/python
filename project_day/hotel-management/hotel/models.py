from django.db import models

class HotelStoreModel(models.Model):
    id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
