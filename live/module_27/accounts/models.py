from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    #
    email = models.CharField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    address_line_1 = models.CharField(blank=True, null=True, max_length=200)
    address_line_2 = models.CharField(blank=True, null=True, max_length=200)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    mobile = models.CharField(blank=True, null=True, max_length=15)

    profile_pucture = models.ImageField(blank=True, null=True, upload_to='user_profile')

    def __str__(self):
        return self.user.username
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'