from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from book.models import BookStoreModel
from book.forms import BookStoreForm

class AddBook(CreateView):
    form_class  = BookStoreForm
    success_url = reverse_lazy('allbooks')
    template_name = 'store_book.html'
    context_object_name = 'form'

class AllBooksList(ListView):
    model = BookStoreModel
    template_name = 'all_books.html'
    context_object_name = 'books'

class UpdateBook(UpdateView):
    pk_url_kwarg = 'id'
    model = BookStoreModel
    form_class = BookStoreForm
    success_url = reverse_lazy('allbooks')
    template_name = 'store_book.html'
    context_object_name = 'form'

class DeleteBook(DeleteView):
    pk_url_kwarg = 'id'
    model = BookStoreModel
    template_name = 'delete_book.html'
    success_url = reverse_lazy('allbooks')
