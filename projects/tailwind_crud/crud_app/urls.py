from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('form/', views.registration.as_view(), name='form'),
    path('update/<int:id>/', views.update.as_view(), name='update'),
    path('delete/<int:id>/', views.delete.as_view(), name='delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
