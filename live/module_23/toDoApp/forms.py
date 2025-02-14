from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

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