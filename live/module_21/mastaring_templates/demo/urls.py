from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reports/', views.reports, name='reports'),
    
    path('data/', views.data, name='data'),
    path('loop/', views.loop, name='loop')
]
