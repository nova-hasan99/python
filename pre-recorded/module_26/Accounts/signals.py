
# this file needed if we want when create a user to automatically create a profile for this user

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, CustomUser

@receiver(post_save, sender = CustomUser)
def create_user_profile(instance, created):
    if created:
        UserProfile.objects.create(user = instance)