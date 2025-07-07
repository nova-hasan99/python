from django.urls import path
from .views import chat_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", chat_view, name="chat"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


