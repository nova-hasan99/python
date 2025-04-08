from django.urls import path, include
from .views import ContactVewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("contacts", ContactVewSet)

urlpatterns = [
    path("", include(router.urls))
]
