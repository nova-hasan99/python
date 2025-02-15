from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Task

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class' : 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class' : 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
            'placeholder': 'Repeat password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs = {
                'class' : 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
                'placeholder': 'Enter your username'
            }),

            'email' : forms.EmailInput(attrs = {
                'class' : 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
                'placeholder': 'Enter your email'
            })
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']
        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : 'Head Line',
                'class' : 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'description' : forms.Textarea(attrs={
                'placeholder' : 'Write About Your Task...',
                'class' : 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'category' : forms.Select(attrs={
                'class' : 'w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'priority' : forms.Select(attrs={
                'class' : 'w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'status' : forms.Select(attrs={
                'class' : 'w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'due_date' : forms.DateInput(attrs={
                'type' : 'date',
                'class' : 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
        }