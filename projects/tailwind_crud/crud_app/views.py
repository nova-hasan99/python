from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from . import models
from . import forms

class home(ListView):
    model = models.Student
    template_name = 'studentData.html'
    context_object_name = 'students'

class registration(CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'studentForm.html'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Registration Successfully!!')
        return super().form_valid(form)
    

class update(UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'studentForm.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Form Update Successfully!!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit"] = True
        return context
    
class delete(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'deleteData.html'
    def form_valid(self, form):
        messages.add_message(self.request, messages.WARNING, 'Form Delete Successfully!!')
        return super().form_valid(form)
    
    

