from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBooksList.as_view(), name='allbooks'),
    path('store_book/', views.AddBook.as_view(), name='storebook'),
    path('update_book/<int:id>', views.UpdateBook.as_view(), name='update_book'),
    path('delete_book/<int:id>', views.DeleteBook.as_view(), name='delete_book')
]
